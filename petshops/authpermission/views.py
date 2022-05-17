from django.shortcuts import render
from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from .serializers import LocationSerializer,SaleSerializer,BreedSerializer
from .serializers import CategorySerializer,CustomerSerializer,EmployeeSerializer,PetstoreSerializer
from rest_framework.viewsets import ModelViewSet

from .serializers import MyTokenObtainPairSerializer,ResetPasswordEmailRequestSerializer
from rest_framework import permissions
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response

from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RequestPasswordResetEmail(ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = ResetPasswordEmailRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Email is valid")
        return Response(serializer.data,status=status.HTTP_200_OK)

class RegistrationView(ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    # permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class LocationModelViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class PetstoreModelViewSet(ModelViewSet):
    serializer_class = PetstoreSerializer
    queryset = Petstore.objects.all()
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class BreedModelViewSet(ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
    permission_classes = [IsAuthenticated]

class EmployeeModelViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]

class CustomerModelViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]

class SaleModelViewSet(ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


