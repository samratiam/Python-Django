from django.contrib import admin
from .models import Location,Petstore,Category,Breed,Employee,Sale,Customer

# Register your models here.
admin.site.register(Location)
admin.site.register(Petstore)
admin.site.register(Category)
admin.site.register(Breed)
admin.site.register(Employee)
admin.site.register(Sale)
admin.site.register(Customer)