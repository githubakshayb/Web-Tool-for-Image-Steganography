from django.db import models
from django.db.models.fields import CharField
# Create your models here.
class users(models.Model):   
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200)
   