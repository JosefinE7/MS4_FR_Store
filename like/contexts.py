from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def like_contents(request):

    like_items = []
    total = 0
    product_count = 0
    like = request.session.get('like', {})

    for item_id, quantity_like in like.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity_like * product.price
        product_count += quantity_like
        like_items.append({
            'item_id': item_id,
            'quantity_like': quantity_like,
            'product': product,
        })

    context = {
        'like_items': like_items,
        'total': total,
        'product_count': product_count,
    }

    return context
