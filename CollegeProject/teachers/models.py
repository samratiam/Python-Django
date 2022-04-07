from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_age = models.IntegerField()
    teacher_address = models.CharField(max_length=100)
