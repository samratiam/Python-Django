from django.shortcuts import render
from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from .serializers import LocationSerializer,SaleSerializer,BreedSerializer,SaleCategorySerializer
from .serializers import CategorySerializer,CustomerSerializer,EmployeeSerializer,PetstoreSerializer
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
    serializer_class = SaleCategorySerializer
    queryset = Breed.objects.all().annotate(salequantity=Sum('sale__total_quantity'),saleprice=Sum('sale__total_price'))

