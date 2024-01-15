from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# /products -> index
def index(request):
    products = Product.objects.all()  # Get all objects from DB
    # Product.objects.filter()  # Filter out objects that are retrieved from DB
    # Product.objects.save()  # Add an object to DB
    # Product.objects.get()  # Get single object from DB

    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')


