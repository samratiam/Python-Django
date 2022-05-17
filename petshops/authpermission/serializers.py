from rest_framework import serializers

from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer
from django.core.exceptions import ValidationError

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.util.encoding import smart_str, force_str,smart_bytes,DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        # token['first_name'] = user.first_name
        return token



from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
import jwt
from datetime import datetime,timedelta
from django.conf import settings

# token = jwt.encode({'email':email,'exp':datetime.utcnow()+timedelta(minutes=5)},
#                        settings.SECRET_KEY,algorithm='HS256')

def token():
    token = jwt.encode({'email':"pudasaini.samrat@gmail.com",'exp':datetime.utcnow()+timedelta(minutes=5)},
                       settings.SECRET_KEY,algorithm='HS256')
    return token

print("Token:",token)


from django.utils.crypto import get_random_string


class ResetPasswordEmailRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    token = serializers.SerializerMethodField()
    
    
    class Meta:
        model = User
        fields = ['email','token']
        
        read_only_fields = ['token']
    
    def get_token(self,instance):
        usertoken = get_random_string(length=32)
        return usertoken
    
    def validate(self,attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print("User id:",user.id)
            
            return attrs
        else:
            raise serializers.ValidationError({'email':('Email doesnot exist')})
    
        return super().validate(attrs)
            
                

# class ResetPasswordSerializer(serializers.ModelSerializer):
#     username=serializers.CharField(max_length=150)
#     password=serializers.CharField(max_length=100)
#     class Meta:
#         model=User
#         fields='__all__'
#         def save(self):
#             username=self.validated_data['username']
#             password=self.validated_data['password']
#             #filtering out whethere username is existing or not, if your username is existing then if condition will allow your username
#             if User.objects.filter(username=username).exists():
#             #if your username is existing get the query of your specific username 
#                 user=User.objects.get(username=username)
#                 #then set the new password for your username
#                 user.set_password(password)
#                 user.save()
#                 return user
#             else:
#                 raise serializers.ValidationError({'error':'please enter valid crendentials'})

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, args):
        email = args.get('email',None)
        username = args.get('username',None)
        password = args.get('password')
        password2 = args.get('password2')

        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email already exists')})
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('Username already exists')})
        
        return super().validate(args)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        user.set_password(validated_data['password'])
        user.save()

        return user


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class PetstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petstore
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    
    

class EmployeeSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Employee
        fields = '__all__'   



class SaleSerializer(serializers.ModelSerializer):
    # breed = serializers.PrimaryKeyRelatedField(many=True,read_only=Tr)
    class Meta:
        model = Sale
        fields = '__all__'