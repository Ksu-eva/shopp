from django.db import models

class Buyer (models.Model):
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    adress = models.TextField(max_length=200)

class Product (models.Model):
    name_pr = models.CharField(max_length=50)
    cost = models.FloatField()

class Order (models.Model):
    date_delivery = models.DateField()
    type_of_delivery = models.CharField(max_length=50)
    adress = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    set_product = models.ManyToManyField(Product)