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
    salequantity = serializers.IntegerField()
    saleprice = serializers.IntegerField()
    
    class Meta:
        model = Breed
        fields = ['id','name','salequantity','saleprice']
    ###To implement Sum of quantity and price from sales in Serializer
    # def get_salequantity(self,obj):
    #     # print("Object type:",list(obj.breed.all()))
    #     s = []
    #     s = obj.sale.filter(breed__name=obj.name).values_list('total_quantity',flat=True)
    #     print(s)
    #     result = sum(s)
    #     return result
        # return obj.sale.annotate(salequantity=Sum('total_quantity')).values('salequantity')
    
    # def get_saleprice(self,obj):
    #     s = []
    #     s = obj.sale.annotate(salequantity=Sum('total_price')).values('salequantity')
    #     print("value of s:",s)
    #     # result = sum(s)
    #     return 5

class SalesetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
    
class SaleRecordSerializer(serializers.ModelSerializer):
    # employee_name = serializers.SerializerMethodField()
    # customers = serializers.SerializerMethodField()
    # sale_quantity = serializers.SerializerMethodField()
    # sale_price = serializers.SerializerMethodField()
    # breed_id = serializers.SerializerMethodField()
    # employee_id = serializers.SerializerMethodField()
    
    data = serializers.SerializerMethodField()
    
    class Meta:
        model = Sale
        fields = ['data']
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['salequantity'] = self.context['salequantity']
    #     representation['saleprice'] = self.context['saleprice']

    #     return representation
    
    # def get_customers(self, obj):
    #     # s = []
    #     # s = Customer.objects.filter(name=request.).values()
    #     # print("Values of s:",s)
    #     print("Object:",obj.all().values_list())
    #     return obj
    
    
    def get_data(self, obj):
        data = self.context
        print("Data:",data)
        return data

    # def get_sale_price(self, obj):
    #     return self.context.get('sale_price')

    # def get_customers(self, obj):
    #     return self.context.get('customers')
    
    # def get_employee_name(self,obj):
    #     return self.context.get('employee_name')
    
    # def get_employee_id(self,obj):
    #     return self.context.get('employee_id')
    
    # def get_breed_id(self,obj):
    #     return self.context.get('breed_id')
    
    

        
    
    
    
    
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
    
    
        


    
  
