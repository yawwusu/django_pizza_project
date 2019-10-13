from django.http import HttpResponse
from django.shortcuts import render
from .models import Serving, Category, Menu, Topping, Order

# Create your views here.
def index(request):
    context = {
        "servings": Serving.objects.all(),
        "categories": Category.objects.all(),
        "menu": Menu.objects.all(),
        "toppings": Topping.objects.all(),
        "orders": Order.objects.all()
    }
    return render(request, "orders/index.html", context)
