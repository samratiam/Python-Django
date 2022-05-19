from django.db import models
from django.core.validators import MaxValueValidator




from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )




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
    customer = models.ForeignKey(Customer,related_name="customer_detail", on_delete=models.SET_NULL,null=True)
    breed = models.ManyToManyField(Breed,related_name="sale")
    
    # def get_breeds(self):
    #     return Breed.objects.filter(breed__name=self)
    
    def __str__(self):
        return self.employee.name