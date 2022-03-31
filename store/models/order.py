from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=50,default='')
    name = models.CharField(max_length=50,default="")
    product_list = models.CharField(max_length=500, default="")
    quantity = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=122, default="")
    email = models.EmailField(max_length=122, default="")
    phone = models.CharField(max_length=15, default="")
    address = models.CharField(max_length=122, default="")
    # city = models.CharField(max_length=50, default="")
    # pincode = models.CharField(max_length=15, default="")
    date = models.DateTimeField(default=datetime.datetime.today)
    payment_id = models.CharField(max_length=100, default="")
    paid = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.email
