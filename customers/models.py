from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=150, help_text=_('name of customer'))
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True, verbose_name='b date')
    phone = models.CharField(max_length=13)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, )
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone}'

    class Meta:
        verbose_name = _('مشتری')
        verbose_name_plural = _('Customers')

    def count_car(self):
        return self.car_set.count()

    count_car.short_description = "his cars"


class Car(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()


class Club(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
