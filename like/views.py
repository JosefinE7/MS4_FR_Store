from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from products.models import Product
from .models import LikeProducts


def view_like(request):
    """ A view to renders the likes contents page """

    return render(request, 'like/view_likes.html')


def like_post(request, product_id):
    product = get_object_or_404(Product, id=request.POST.get('like_button'))
    likes = 
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('product_detail'), args=[str(product_id)])
