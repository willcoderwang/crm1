from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=128)
    price = models.FloatField()
    category = models.CharField(max_length=64, choices=CATEGORY)
    description = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    # customer =
    # product =
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=64, choices=STATUS)
