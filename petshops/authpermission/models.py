import jwt
from datetime import datetime,timedelta
from django.conf import settings
from django.contrib.auth.models import User

user = User.objects.get(email="pudasaini.samrat@gmail.com")
payload = jwt_payload_handler(user)
token = jwt.encode(payload,settings.SECRET_KEY)


print("Token:",token)




# from django.db import models
# from django.core.validators import MaxValueValidator

# class Location(models.Model):
#     street = models.CharField(max_length=125)
#     city = models.CharField(max_length=125)
#     country = models.CharField(max_length=125)
    
#     def __str__(self):
#         return self.city
    

# class Petstore(models.Model):
#     name = models.CharField(max_length=125)
#     website = models.URLField()
#     contact=models.CharField(max_length=10)
#     email = models.EmailField()
    
#     location = models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
    
#     def __str__(self):
#         return self.name
    
# class Category(models.Model):
#     name = models.CharField(max_length=125)
    
#     def __str__(self):
#         return self.name

# class Breed(models.Model):
#     name = models.CharField(max_length=125)
#     quantity = models.IntegerField()
#     price = models.FloatField()
    
#     category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
#     petstore = models.ForeignKey(Petstore,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name
    
# class Employee(models.Model):
#     name = models.CharField(max_length=125)
#     role = models.CharField(max_length=125)
#     contact=models.CharField(max_length=10)
#     email = models.EmailField()
#     address = models.CharField(max_length=125)
    
#     petstore = models.ForeignKey(Petstore,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name

# class Customer(models.Model):
#     name = models.CharField(max_length=125)
#     contact=models.CharField(max_length=10)
#     email = models.EmailField()
#     address = models.CharField(max_length=125)
    
#     def __str__(self):
#         return self.name

# class Sale(models.Model):
#     total_quantity = models.IntegerField()
#     total_price = models.FloatField()
#     sale_date = models.DateField(auto_now=True)
    
#     employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
#     customer = models.ForeignKey(Customer,related_name="customer_detail", on_delete=models.SET_NULL,null=True)
#     breed = models.ManyToManyField(Breed,null=True)
    
#     def __str__(self):
#         return self.employee.name


###Send Email

# from django.dispatch import receiver
# from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
# from django.core.mail import send_mail  


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

#     email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="Samrat's Website"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "samrat.pudasaini@gmail.com",
#         # to:
#         [reset_password_token.user.email]
#     )

##From  Django Rest Password Reset Docs
# from django.core.mail import EmailMultiAlternatives
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from django.urls import reverse

# from django_rest_passwordreset.signals import reset_password_token_created


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     """
#     Handles password reset tokens
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender: View Class that sent the signal
#     :param instance: View Instance that sent the signal
#     :param reset_password_token: Token Model Object
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     # send an e-mail to the user
#     context = {
#         'current_user': reset_password_token.user,
#         'username': reset_password_token.user.username,
#         'email': reset_password_token.user.email,
#         'reset_password_url': "{}?token={}".format(
#             instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
#             reset_password_token.key)
#     }

#     # render email text
#     email_html_message = render_to_string('email/user_reset_password.html', context)
#     email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

#     msg = EmailMultiAlternatives(
#         # title:
#         "Password Reset for {title}".format(title="Samrat Website"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "noreply@localhost.local",
#         # to:
#         [reset_password_token.user.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     msg.send()
