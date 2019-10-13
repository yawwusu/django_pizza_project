from django.contrib import admin
from .models import Serving, Category, Menu, Topping, Order

# Register your models here.
admin.site.register(Serving)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Topping)
admin.site.register(Order)
