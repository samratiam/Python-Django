from django.db import models
from teachers.models import Teachers
# Create your models here.


class Courses(models.Model):
    course_name = models.CharField(max_length=80)
    course_code = models.CharField(max_length=10)
    course_faculty = models.CharField(max_length=50)
    course_teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
