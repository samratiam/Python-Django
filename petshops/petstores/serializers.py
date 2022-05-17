from rest_framework import serializers

from .models import Location,Petstore,Category,Breed,Employee,Sale,Customer

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
        fields = ['id','total_quantity','total_price','employee','customer','breed']
    
    
    # employees = EmployeeSerializer
    # breed = BreedSerializer(many=True)
    customer = CustomerSerializer()

    def create(self,validated_data):
        customer_data = validated_data.pop('customer')
        breed_data = validated_data.pop('breed')
        print("Breed:",breed_data)
        print("Breed id:",breed_data)
        print("Breed type:",type(breed_data))
        
        # b = Breed.objects.filter(name=breed_data)
        # print("Fiter: ",b)
        
        breeds = Breed.objects.filter(name=breed_data)
        customer = Customer.objects.create(**customer_data)
        
        sale = Sale.objects.create(customer=customer,**validated_data)
        sale.breed.set(breed_data)
        print("Sale breed:",sale.breed)
        
        return sale
    
    
        
    # def create(self, validated_data):
    #     employees_data = validated_data.pop('employees')
    #     sale = Sale.objects.create(**validated_data)
    #     for employee_data in employees_data:
    #         Employee.objects.create(sale=sale,**employee_data)
    #     return sale

    
  
