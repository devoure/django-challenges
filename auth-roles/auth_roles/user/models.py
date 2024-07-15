from django.db import models
from django.contrib.auth import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=256)
    ..
