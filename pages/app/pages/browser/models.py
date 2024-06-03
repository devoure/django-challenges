from django.db import models


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=40)
    student_id = models.CharField(max_length=20)
    grade = models.CharField(max_length=1)
