from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=128)
    customer_surname = models.CharField(max_length=128)
    e_mail = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customer_name


class Category(models.Model):
    category_name = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category_id = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.product_name} - {self.product_price} PLN'


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.customer_id}: {self.product_id}'

class History(models.Model):
    person = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
