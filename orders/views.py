from django.http import HttpResponse
from django.shortcuts import render
from .models import Regular, Silician, Subs, Pasta, Salads, DinnerPlatters , Toppings

# Create your views here.
def index(request):
    context = {
        "regular": Regular.objects.all(),
        "silician": Silician.objects.all(),
        "subs": Subs.objects.all(),
        "pasta": Pasta.objects.all(),
        "salads": Salads.objects.all(),
        "dinnerplatters": DinnerPlatters.objects.all(),
        "toppings": Toppings.objects.all()
    }
    return render(request, "orders/index.html", context)
