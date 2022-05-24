from django.shortcuts import render
from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from .serializers import LocationSerializer,SaleSerializer,BreedSerializer,SaleCategorySerializer
from .serializers import CategorySerializer,CustomerSerializer,EmployeeSerializer,PetstoreSerializer
from .serializers import SalesetSerializer,SaleRecordSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

class LocationModelViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class PetstoreModelViewSet(ModelViewSet):
    serializer_class = PetstoreSerializer
    queryset = Petstore.objects.all()

class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class BreedModelViewSet(ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()

class EmployeeModelViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class CustomerModelViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class SaleModelViewSet(ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, many=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        sale_date = self.request.query_params.get('sale_date')
        
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        
        if sale_date is not None:
            queryset = Sale.objects.filter(sale_date__iexact=sale_date)
        
        elif start_date is not None and end_date is not None:
            queryset = Sale.objects.filter(sale_date__range=(start_date,end_date))
        
        else:
            queryset = Sale.objects.all().order_by('-id')
        serializer_class = SaleSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
   
    
    # def list(self,request):
    #     start_date = self.request.query_params.get('start_date')
    #     end_date = self.request.query_params.get('end_date')
    #     if start_date is not None and end_date is not None:
    #         queryset = Sale.objects.filter(sale_date__range=(start_date,end_date))
    #     serializer_class = SaleSerializer(queryset, many=True)
    #     return Response(serializer_class.data)
        
from django.db.models import Sum
class SaleCategoryModelViewSet(ModelViewSet):
    serializer = SaleCategorySerializer
    queryset = Breed.objects.all().annotate(salequantity=Sum('sale__total_quantity'),saleprice=Sum('sale__total_price'))

from django.core.exceptions import ValidationError
class SalesetModelViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SalesetSerializer
    
    def get_object(self, obj_id):
        try:
            return Sale.objects.get(id=obj_id)
        except (Sale.DoesNotExist, ValidationError):
            raise status.HTTP_400_BAD_REQUEST
    
    def validate_ids(self, id_list):
        for id in id_list:
            try:
                Sale.objects.get(id=id)
            except (Sale.DoesNotExist, ValidationError):
                raise status.HTTP_400_BAD_REQUEST
        return True
    
    
    def put(self, request, *args, **kwargs):
       data = request.data
       instances = []
       for temp_dict in data:
            id = temp_dict['id']
            obj = self.queryset.get(id=id)
            obj.total_quantity = temp_dict['total_quantity']
            obj.total_price = temp_dict['total_price']
            obj.Employee = temp_dict['employee'] 
            obj.Customer = temp_dict['customer']
            obj.Breed = temp_dict['breed'] 
            obj.save()
            instances.append(obj)
       serializer = SalesetSerializer(instances, many=True)
       return Response(serializer.data)
    
class SaleRecordModelViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleRecordSerializer
    
    def list(self, request):
        breed = self.request.query_params.get('breed')
        employee = self.request.query_params.get('employee')
        
        if breed is not None and employee is not None:
            # queryset = Sale.objects.filter(employee__name__iexact=employee,breed__name__iexact=breed)
            b = Sale.objects.filter(employee__name__iexact=employee,breed__name__iexact=breed).values_list('total_quantity',flat=True)
                # print("Value of b:",b)
            print("Sum of b:",sum(b))
            sale_quantity = sum(b)
            
            c = []
            c = Sale.objects.filter(employee__name__iexact=employee,breed__name__iexact=breed).values_list('total_price',flat=True)
            print("Sum of c:",sum(c))
            sale_price = sum(c)
            
            
            customers = Sale.objects.filter(employee__name__iexact=employee,breed__name__iexact=breed).values('customer_id','customer__name','total_quantity','total_price')
            employee_id = Sale.objects.filter(employee__name__iexact=employee).values_list('employee__id',flat=True).distinct()
            breed_id = Sale.objects.filter(breed__name__iexact=breed).values_list('breed__id',flat=True).distinct()
            # employee_name = Sale.objects.get(employee__name__iexact=employee).values('employee__name')
            
            
            data = {'sale_quantity':sale_quantity,'sale_price':sale_price,'customers':customers,'employee_name':employee,'employee_id':employee_id[0],'breed_id':breed_id[0]}
            
                        
            queryset = Sale.objects.all()
            serializer_class = SaleRecordSerializer(queryset, context=data)
        else:
            queryset = Sale.objects.all().order_by('-id')
            serializer_class = SaleRecordSerializer(queryset, many=True)
        return Response(serializer_class.context)
    
    
    ###Another way
    # def put(self, request, *args, **kwargs):
    #     for i in request.data:        
    #         instance = Sale.objects.get(id=i['id'])                
    #         serializer = SalesetSerializer(instance, data=i)
    #         if serializer.is_valid(raise_exception=True):
    #             self.perform_update(serializer)            
    #         # return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    
  
    
    # def put(self, request, *args, **kwargs):
    #     # partial = kwargs.pop('partial', False)
    #     data = request.data
    #     print("Type of data:",type(data))
        
    #     print("Data:",data)
    #     instances = []
        
    #     for temp_dict in data:
    #         id = temp_dict['id']
    #         total_price = temp_dict['total_price']
    #         total_quantity = temp_dict['total_quantity']
    #         employee = temp_dict['employee']
    #         customer = temp_dict['customer']
    #         breed = temp_dict['breed']
    #         # sale_date = temp_dict['sale_date']
    #         print("ID:",id)
    #         obj = self.get_object(id)
    #         obj.total_price = total_price
    #         obj.total_quantity = total_quantity
    #         for i in range(employee):
    #             obj.employee = Employee.objects.get(id=employee[i])
    #         for i in range(customer):
    #             obj.customer = Customer.objects.get(id=customer[i])
    #         for i in range(breed):
    #             obj.breed = Breed.objects.get(id=breed[i])
    #         # obj.sale_date = sale_date
    #         obj.save()
    #         instances.append(obj)
    #     print("Temp dict:",temp_dict)
    #     serializer_class = SalesetSerializer(instances,many=True)
    #     # for instance in instances:
    #         # serializer = self.get_serializer(instances, data=request.data, partial=partial,many=True)
    #         # serializer.is_valid(raise_exception=True)
    #         # self.perform_update(serializer)
    #     return Response(serializer_class.data)
    
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

