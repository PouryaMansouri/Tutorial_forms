from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=150, help_text='name of customer')
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True, verbose_name='b date')
    phone = models.CharField(max_length=13)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, )
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class Car(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=120)
