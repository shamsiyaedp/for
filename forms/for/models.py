from django.db import models

# Create your models here.
class form(models.Model):
    password=models.IntegerField()
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField
