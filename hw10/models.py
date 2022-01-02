from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    product = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Supplier(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE)
