from django.shortcuts import render
from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from .serializers import LocationSerializer,SaleSerializer,BreedSerializer
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
    
    def list(self, request):
        queryset = Sale.objects.all()
        sale_date = self.request.query_params.get('sale_date')
        if sale_date is not None:
            queryset = queryset.filter(sale_date__iexact=sale_date)
        serializer_class = SaleSerializer(queryset, many=True)
        return Response(serializer_class.data)

