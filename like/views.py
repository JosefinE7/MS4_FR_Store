from django.shortcuts import render, redirect


def view_like(request):
    """ A view to renders the like contents page """

    return render(request, 'like/like.html')


def add_to_like(request, item_id):
    """ Add a product to the like category """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    like = request.session.get('like', {})

    if item_id in list(like.keys()):
        like[item_id] += quantity
    else:
        like[item_id] = quantity

    request.session['like'] = like
    print(request.session['like'])
    return redirect(redirect_url)
