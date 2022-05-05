from django.shortcuts import render
from .models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from .serializers import LocationSerializer,SaleSerializer,BreedSerializer
from .serializers import CategorySerializer,CustomerSerializer,EmployeeSerializer,PetstoreSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

# Create your views here.
class LocationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def update(self,request,pk):
        id = pk
        location = Location.objects.get(pk=id)
        serializer = LocationSerializer(location, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        location = Location.objects.get(pk=id)
        serializer = LocationSerializer(location, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        location = Location.objects.get(pk=id)
        location.delete()
        return Response({'msg':'Data deleted'})

class PetstoreViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = PetstoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = Petstore.objects.all()
        serializer = PetstoreSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = Petstore.objects.all()
        petstore = get_object_or_404(queryset, pk=pk)
        serializer = PetstoreSerializer(petstore)
        return Response(serializer.data)

    def update(self,request,pk):
        id = pk
        petstore = Petstore.objects.get(pk=id)
        serializer = PetstoreSerializer(petstore, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        petstore = Petstore.objects.get(pk=id)
        serializer = PetstoreSerializer(petstore, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self,request,pk):
        id = pk
        petstore = Petstore.objects.get(pk=id)
        petstore.delete()
        return Response({'msg':'Data deleted'})