from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Serving, Category, Menu, Topping, Order

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "servings": Serving.objects.all(),
        "categories": Category.objects.all(),
        "menu": Menu.objects.all(),
        "toppings": Topping.objects.all(),
        "orders": Order.objects.all(),
        "user": request.user
    }
    return render(request, "orders/index.html", context)


def register(request):
    return render(request, "orders/register.html")


def success(request):
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
    return render(request, "orders/login.html", {"message": "Successfully registered, enter details to login"})


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})


def add_to_cart(request):
    try:
        menu_id = int(request.POST["maindish"])
        menu = Menu.objects.get(pk=menu_id)
    except KeyError:
        return render(request, "orders/error.html", {"message": "No selection."})
    except menu.DoesNotExist:
        return render(request, "orders/error.html", {"message": "No such menu item."})
    order = Order(name = request.user.first_name)
    order.save()
    order.menuitem.add(menu)
    return HttpResponseRedirect(reverse("index"))


def order(request):
    # Order = Order.objects.get(pk=Order_id)
    context = {
        "orders": Order.objects.all()
    }
    return render(request, "orders/order.html", context)
