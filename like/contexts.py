from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def like_contents(request):

    like_items = []
    like = request.session.get('like', {})

    for item_id in like.items():
        product = get_object_or_404(Product, pk=item_id)
        like_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'like_items': like_items,
    }

    return context
