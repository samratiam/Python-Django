from django.db import models
from .models import Teacher
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=80)
    course_code = models.CharField(max_length=10)
    course_faculty = models.CharField(max_length=50)
    course_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
