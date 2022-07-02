from secrets import choice
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    date_created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY=(
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=60)
    price = models.FloatField()
    category = models.CharField(max_length=50, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True)
    date_created = models.TimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of Delivery', 'Out of Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_created = models.TimeField(auto_now_add=True) 
    status = models.CharField(max_length=200, choices=STATUS)       