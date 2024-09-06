from django.db import models

from tracking_system.generate_dummy_data import username


# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  active = models.BooleanField(default=True)
  image = models.ImageField(upload_to='products/')
  def __str__(self):
    return self.name
  class Meta:
    ordering = ['name']


class User(models.Model):
  name = models.CharField(max_length=100)
  products = models.ForeignKey(Product, models.PROTECT)
