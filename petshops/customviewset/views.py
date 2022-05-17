from django.shortcuts import render
from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from petstores.serializers import LocationSerializer,SaleSerializer,BreedSerializer
from petstores.serializers import CategorySerializer,CustomerSerializer,EmployeeSerializer,PetstoreSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class LocationModelViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    
    def get_queryset(self):
        location = Location.objects.all()
        return location
    
    # def retrieve(self, r)
    
    def create(self, request, *args, **kwargs):
        location_data = request.data

        new_location = Location.objects.create(street=location_data["street"], city=location_data["city"], country=location_data["country"])

        new_location.save()

        serializer = LocationSerializer(new_location)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        location = self.get_object()
        location.delete()
        response_message = {"message": "Item has been deleted"}
        return Response(response_message)
    
    def update(self, request, *args, **kwargs):
        location_object = self.get_object()
        data = request.data
        location_object.street = data["street"]
        location_object.city = data["city"]
        location_object.country = data["country"]

        location_object.save()

        serializer =LocationSerializer(location_object)

        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        location_object = self.get_object()
        data = request.data

        # location_object.street = data["street"]
        # location_object.city = data["city"]
        # location_object.country = data["country"]

        # location_object.save()

        serializer =LocationSerializer(location_object,data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    
        
# class PetstoreModelViewSet(ModelViewSet):
#     serializer_class = PetstoreSerializer
#     queryset = Petstore.objects.all()

# class CategoryModelViewSet(ModelViewSet):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()

# class BreedModelViewSet(ModelViewSet):
#     serializer_class = BreedSerializer
#     queryset = Breed.objects.all()

# class EmployeeModelViewSet(ModelViewSet):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

# class SaleModelViewSet(ModelViewSet):
#     serializer_class = SaleSerializer
#     queryset = Sale.objects.all()

# class CustomerModelViewSet(ModelViewSet):
#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()



