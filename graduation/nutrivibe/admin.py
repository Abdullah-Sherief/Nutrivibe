from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Products)
admin.site.register(Exercises)
admin.site.register(Recipes)
admin.site.register(Orders)
admin.site.register(OrdersItems)
admin.site.register(UserCart)
admin.site.register(UserCartItems)