from rest_framework import serializers

from petstores.models import Location,Petstore,Category,Breed,Employee,Sale,Customer

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
    # breed_name = serializers.ReadOnlyField(source=Sale.breed)
    breed_name = serializers.SerializerMethodField('get_breed_name')
    # breed_name = SaleSerializer(many=True,source=breed_name)
    
    class Meta:
        model = Sale
        fields = ['id','total_quantity','total_price','employee','customer','breed','breed_name','sale_date']
        # extra_kwargs = {'breed_name': {'read_only': True}}

        
        # fields = '__all__'
        # depth = 1
    
    def get_breed_name(self,obj):
        # print("Object type:",list(obj.breed.all()))
        return obj.breed.values_list('name',flat=True)
    
    
    # customer = CustomerSerializer()

    # def create(self,validated_data):
    #     customer_data = validated_data.pop('customer')
    #     breed_data = validated_data.pop('breed')
    #     print("Breed:",breed_data)
    #     print("Breed id:",breed_data)
    #     print("Breed type:",type(breed_data))
        
        
    #     breeds = Breed.objects.filter(name=breed_data)
    #     customer = Customer.objects.create(**customer_data)
        
    #     sale = Sale.objects.create(customer=customer,**validated_data)
    #     sale.breed.set(breed_data)
    #     print("Sale breed:",sale.breed)
        
    #     return sale
    
    
        


    
  
