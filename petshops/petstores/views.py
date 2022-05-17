from django.shortcuts import render
from .models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from .serializers import LocationSerializer,SaleSerializer,BreedSerializer
from .serializers import CategorySerializer,CustomerSerializer,EmployeeSerializer,PetstoreSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter
from .pagination import MyLimitOffsetPagination


from django.shortcuts import get_object_or_404

# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    # serializer_class = LocationSerializer
    # queryset = Location.objects.all()
    
    # def get_queryset(self):
    #     queryset = Location.objects.all()
    #     serializer_class = LocationSerializer
    #     city = self.request.query_params.get('city')
    #     if city is not None:
    #         queryset = queryset.filter(city__iexact=city)
    #         # print("List of cities:",list(queryset))
    #     return Response(self.serializer_class(query_set, many=True).data,
    #                     status=status.HTTP_200_OK)
    
    
    def create(self, request):
        serializer_class = LocationSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Location.objects.all()
        city = self.request.query_params.get('city')
        if city is not None:
            queryset = queryset.filter(city__iexact=city)
        serializer_class = LocationSerializer(queryset, many=True)
        return Response(serializer_class.data)
        
    
        
    
    def retrieve(self, request, pk = None):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer_class = LocationSerializer(location)
        return Response(serializer_class.data)

    def update(self,request,pk):
        id = pk
        location = Location.objects.get(pk=id)
        serializer_class = LocationSerializer(location, data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        location = Location.objects.get(pk=id)
        serializer_class = LocationSerializer(location, data = request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        location = Location.objects.get(pk=id)
        location.delete()
        return Response({'msg':'Data deleted'})

class PetstoreViewSet(viewsets.ModelViewSet):
    def create(self, request):
        serializer_class = PetstoreSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Petstore.objects.all()
        serializer_class = PetstoreSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk = None):
        queryset = Petstore.objects.all()
        petstore = get_object_or_404(queryset, pk=pk)
        serializer_class = PetstoreSerializer(petstore)
        return Response(serializer_class.data)

    def update(self,request,pk):
        id = pk
        petstore = Petstore.objects.get(pk=id)
        serializer_class = PetstoreSerializer(petstore, data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        petstore = Petstore.objects.get(pk=id)
        serializer_class = PetstoreSerializer(petstore, data = request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        petstore = Petstore.objects.get(pk=id)
        petstore.delete()
        return Response({'msg':'Data deleted'})

class CategoryViewSet(viewsets.ModelViewSet):
    def create(self, request):
        serializer_class = CategorySerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk = None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer_class = CategorySerializer(category)
        return Response(serializer_class.data)

    def update(self,request,pk):
        id = pk
        category = Category.objects.get(pk=id)
        serializer_class = CategorySerializer(category, data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        category = Category.objects.get(pk=id)
        serializer_class = CategorySerializer(category, data = request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        category = Category.objects.get(pk=id)
        category.delete()
        return Response({'msg':'Data deleted'})

class BreedViewSet(viewsets.ModelViewSet):
    def create(self, request):
        serializer_class = BreedSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Breed.objects.all()
        serializer_class = BreedSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk = None):
        queryset = Breed.objects.all()
        breed = get_object_or_404(queryset, pk=pk)
        serializer_class = BreedSerializer(breed)
        return Response(serializer_class.data)

    def update(self,request,pk):
        id = pk
        breed = Breed.objects.get(pk=id)
        serializer_class = BreedSerializer(breed, data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        breed = Breed.objects.get(pk=id)
        serializer_class = BreedSerializer(breed, data = request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        breed = Breed.objects.get(pk=id)
        breed.delete()
        return Response({'msg':'Data deleted'})

class EmployeeViewSet(viewsets.ModelViewSet):
    def create(self, request):
        serializer_class = EmployeeSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk = None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer_class = EmployeeSerializer(employee)
        return Response(serializer_class.data)

    def update(self,request,pk):
        id = pk
        employee = Employee.objects.get(pk=id)
        serializer_class = EmployeeSerializer(employee, data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        employee = Employee.objects.get(pk=id)
        serializer_class = EmployeeSerializer(employee, data = request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        employee = Employee.objects.get(pk=id)
        employee.delete()
        return Response({'msg':'Data deleted'})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = MyLimitOffsetPagination
    filter_backends = [OrderingFilter]
    
    ordering_fields = ['id']
    ordering = ['-id']
    
    def create(self, request):
        serializer_class = CustomerSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
        
    def retrieve(self, request, pk = None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer_class = CustomerSerializer(customer)
        return Response(serializer_class.data)

    def update(self,request,pk):
        id = pk
        customer = Customer.objects.get(pk=id)
        serializer_class = CustomerSerializer(customer, data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        customer = Customer.objects.get(pk=id)
        serializer_class = CustomerSerializer(customer, data = request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        customer = Customer.objects.get(pk=id)
        customer.delete()
        return Response({'msg':'Data deleted'})

class SaleViewSet(viewsets.ModelViewSet):
    def create(self, request):
        serializer_class =SaleSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset =Sale.objects.all()
        serializer_class =SaleSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk = None):
        queryset =Sale.objects.all()
        sale = get_object_or_404(queryset, pk=pk)
        serializer_class =SaleSerializer(sale)
        return Response(serializer_class.data)

    def update(self,request,pk):
        id = pk
        sale =Sale.objects.get(pk=id)
        serializer_class =SaleSerializer(sale, data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        sale =Sale.objects.get(pk=id)
        serializer_class =SaleSerializer(sale, data = request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        sale =sale.objects.get(pk=id)
        sale.delete()
        return Response({'msg':'Data deleted'})



