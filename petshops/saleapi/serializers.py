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




# class SaleListSerializer(serializers.ListSerializer):
#     def update(self, instance, validated_data):
        
#         # import ipdb
#         # ipdb.set_trace()
        
#         # Maps for id->instance and id->data item.
#         sale_mapping = {sale.id: sale for sale in instance}
#         data_mapping = {item['id']: item for item in validated_data}

#         # Perform creations and updates.
#         ret = []
#         for sale_id, data in data_mapping.items():
#             sale = book_mapping.get(sale_id, None)
#             if sale is None:
#                 ret.append(self.child.create(data))
#             else:
#                 print("After Else------------")
#                 ret.append(self.child.update(sale, data))
#                 print("End of Else------------")
     
#         return ret



class SaleSerializer(serializers.ModelSerializer):
    # breed_name = serializers.ReadOnlyField(source=Sale.breed)
    # id = serializers.IntegerField()
    breed_name = serializers.SerializerMethodField('get_breed_name')
    # breed_name = SaleSerializer(many=True,source=breed_name)
    
    class Meta:
        # list_serializer_class = SaleListSerializer
        model = Sale
        fields = ['id','total_quantity','total_price','employee','customer','breed','breed_name','sale_date']
        # extra_kwargs = {'breed_name': {'read_only': True}}

        
        # fields = '__all__'
        # depth = 1
    
    def get_breed_name(self,obj):
        # print("Object type:",list(obj.breed.all()))
        return obj.breed.values_list('name',flat=True)
    

from django.db.models import Sum
class SaleCategorySerializer(serializers.ModelSerializer):
    total_quantity = list(Breed.objects.annotate(salequantity=Sum('sale__total_quantity')).values('salequantity'))
    total_price = list(Breed.objects.annotate(saleprice=Sum('sale__total_price')).values('saleprice'))
    print("total quantity:",total_quantity)
    print("total price:",total_price)
    
    # salequantity = serializers.SerializerMethodField()
    # saleprice = serializers.SerializerMethodField()
    
    
    # def get_salequantity(self,obj):
    #     return self.objects.annotate(salequantity=Sum('sale__total_quantity')).values('salequantity')
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['salequantity'] = instance.sale.all().total_quantity.sum()

    #     return representation
    
    salequantity = serializers.SerializerMethodField()
    saleprice = serializers.SerializerMethodField()
    
    class Meta:
        model = Breed
        fields = ['id','name','salequantity','saleprice']

    def get_salequantity(self,obj):
        # print("Object type:",list(obj.breed.all()))
        s = []
        s = obj.sale.annotate(salequantity=Sum('total_quantity')).values_list('salequantity',flat=True)
        result = sum(s)
        return result
        # return obj.sale.annotate(salequantity=Sum('total_quantity')).values('salequantity')
    
    def get_saleprice(self,obj):
        s = []
        s = obj.sale.annotate(salequantity=Sum('total_price')).values_list('salequantity',flat=True)
        result = sum(s)
        return result
        
    
    
    
    
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
    
    
        


    
  
