from django.db import models
from django.utils import timezone

class Service(models.Model):
    service_name = models.CharField(max_length=100)    
    inventory_level = models.IntegerField()

    def __str__(self):
        return self.service_name

class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    transaction_quantity = models.IntegerField()
    transaction_date = models.DateField()

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    initial_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_date = models.DateTimeField(default=timezone.now)
    ready_by_date = models.DateTimeField()

    def __str__(self):
        return f"Order #{self.id}"
