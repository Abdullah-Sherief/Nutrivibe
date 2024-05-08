from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    weight = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    tag_name = models.CharField(max_length=100)
    stars = models.IntegerField(default=0, null=True, blank=True)
    calories = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Exercises(models.Model):
    type = models.CharField(max_length=100)
    video_url = models.URLField()

    def __str__(self):
        return self.type
    

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    image_url = models.URLField()
    video_url = models.URLField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Products, through='OrdersItems')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f"Sale #{self.pk}"

class OrdersItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.item.name} - Quantity: {self.quantity}"

class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Products, through='UserCartItems')

class UserCartItems(models.Model):
    order = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.item.name} - Quantity: {self.quantity}"