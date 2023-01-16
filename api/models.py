from django.db import models


# Create your models here.
class Customers(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    AboutUs = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                     ('NON IT', 'NON IT'),
                                                     ('MOBILE PHONE', 'MOBILE PHONE')))
    add_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    description = models.TextField()
    parameter = models.CharField(max_length=100, choices=(('kg', 'kg'),
                                                     ('ltr', 'ltr'),
                                                     ('mtr', 'mtr')))
    add_date = models.DateTimeField(auto_now=True)
    Avaliable = models.BooleanField(default=True)
    customer = models.ForeignKey(Customers , on_delete=models.CASCADE)
