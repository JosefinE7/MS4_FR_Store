from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from products.models import Product

from .models import Likes


def like(request, username, product_id):
    user_liking = request.user
    product = Product.objects.get(product_id=product_id)
    like = Likes.objects.get(user=)
