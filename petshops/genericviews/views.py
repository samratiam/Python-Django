from django.shortcuts import render
from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from petstores.serializers import LocationSerializer,SaleSerializer,BreedSerializer
from petstores.serializers import CategorySerializer,CustomerSerializer,EmployeeSerializer,PetstoreSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LocationListCreateAPIView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class PetstoreListCreateAPIView(ListCreateAPIView):
    queryset = Petstore.objects.all()
    serializer_class = PetstoreSerializer

class PetstoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Petstore.objects.all()
    serializer_class = PetstoreSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BreedListCreateAPIView(ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SaleListCreateAPIView(ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

















