from django.db import models
from django.core.validators import MaxValueValidator

class Location(models.Model):
    street = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    country = models.CharField(max_length=125)
    
    def __str__(self):
        return self.city
    

class Petstore(models.Model):
    name = models.CharField(max_length=125)
    website = models.URLField()
    contact=models.CharField(max_length=10)
    email = models.EmailField()
    
    location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=125)
    
    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=125)
    quantity = models.IntegerField()
    price = models.FloatField()
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    petstore = models.ForeignKey(Petstore,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=125)
    role = models.CharField(max_length=125)
    contact=models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=125)
    
    petstore = models.ForeignKey(Petstore,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=125)
    contact=models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=125)
    
    def __str__(self):
        return self.name

class Sale(models.Model):
    total_quantity = models.IntegerField()
    total_price = models.FloatField()
    sale_date = models.DateField(auto_now=True)
    
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    breed = models.ManyToManyField(Breed)
    
    def __str__(self):
        return self.breed.name