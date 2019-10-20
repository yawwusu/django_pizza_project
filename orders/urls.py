from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("success", views.success, name="success"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("cart", views.add_to_cart, name="cart"),
    path("order", views.order, name="order")    
]
