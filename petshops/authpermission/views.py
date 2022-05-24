from django.shortcuts import render
from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from .serializers import LocationSerializer,SaleSerializer,BreedSerializer,RegisterUserSerializer
from .serializers import CategorySerializer,CustomerSerializer,EmployeeSerializer,PetstoreSerializer
from rest_framework.viewsets import ModelViewSet

from .serializers import MyTokenObtainPairSerializer,ResetPasswordEmailRequestSerializer
from rest_framework import permissions
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RequestPasswordResetEmail(ModelViewSet):
    # queryset = User.objects.all()
    
    
    serializer_class = ResetPasswordEmailRequestSerializer()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Email is valid")
        return Response(serializer.data,status=status.HTTP_200_OK)

class RegistrationView(ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    
    def create(self,request):
        data = request.data
        print("Validated data:",data)
        # serializer_class = RegisterUserSerializer
        # serializer.is_valid(raise_exception=True)
        # username = serializer.validated_data['username']
        # password = serializer.validated_data['password']
        # user = User.objects.create(username=username,password=password)
        # user.set_password(validated_data['password'])
        # user.save()
        # for user in User.objects.all():
        #     Token.objects.get_or_create(user=user)
        # user = serializer.validated_data['username']
        
        user = User.objects.create(
            username=data['username']           
        )

        user.set_password(data['password'])
        user.save()
        
        print("User:",request.user)
        
        token, created = Token.objects.get_or_create(user=user)
        print("Token key:",token.key)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })
    

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


