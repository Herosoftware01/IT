from django.shortcuts import render
from .models import VueYarnStock

# Create your views here.
# def home(request):
#     data = VueYarnStock.objects.all()
#     return render(request, "home.html", {"data":data})


def home(request):
    data = VueYarnStock.objects.using('mssql').all()
    return render(request, "home.html", {"data": data})