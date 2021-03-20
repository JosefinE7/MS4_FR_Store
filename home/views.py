from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def all_products(request):
    """ A view to show all products, including sorting and seach queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
