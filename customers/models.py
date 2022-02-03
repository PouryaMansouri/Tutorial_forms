from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=150, )
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=13)
    address = models.TextField(null=True, blank=True)
