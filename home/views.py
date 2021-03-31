from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page and new arrivals items """

    products = Product.objects.filter(category__name='earrings')

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about page  """

    return render(request, 'home/about.html')
