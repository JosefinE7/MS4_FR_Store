from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from django.db.models import Avg

from profiles.models import UserProfile

from .models import Product, Category, RatingProducts
from .forms import ProductForm, RatingProductsForm


def all_products(request):
    """ A view to show all products, including sorting and seach queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any seach criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    rating_products = RatingProducts.objects.filter(product=product)
    rating_avg = rating_products.aggregate(Avg('rate'))
    rating_count = rating_products.count()
    favorited = False

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        if profile.favorites.filter(id=product_id).exists():
            favorited = True

    context = {
        'product': product,
        'rating_products': rating_products,
        'rating_avg': rating_avg,
        'rating_count': rating_count,
        'favorited': favorited,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ View that allows admin to add products to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please make sure form is filled in correctly!')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Gives the ability for admin to edit products in store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Product failed to update. Please make sure form is filled in correctly!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Gives the ability for admin to delete products in store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def rating_products(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    if request.method == 'POST':
        form = RatingProductsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.product = product
            rate.save()
            messages.success(request, 'Your review has been added!')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = RatingProductsForm()

    template = 'products/rating_products.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def liked_product(request):
    product = Product.objects.all()
    user = request.user
    profile = UserProfile.objects.get(user=user)

    like_list = profile.favorites.all()

    template = 'products/liked_product.html'
    context = {
        'profile': profile,
        'product': product,
        'like_list': like_list,
    }

    return render(request, template, context)


@login_required
def add_product_to_like(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    profile = UserProfile.objects.get(user=user)

    profile.favorites.add(product)

    return redirect(reverse('product_detail', args=[product.id]))
