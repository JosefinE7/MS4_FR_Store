from django.shortcuts import render, redirect


def view_like(request):
    """ A view to renders the like contents page """

    return render(request, 'like/like.html')


def add_to_like(request, item_id):
    """ Add a product to the like category """

    quantity_like = int(request.POST.get('quantity_like'))
    redirect_url = request.POST.get('redirect_url')
    like = request.session.get('like', {})

    if item_id in list(like.keys()):
        like[item_id] += quantity_like
    else:
        like[item_id] = quantity_like

    request.session['like'] = like
    print(request.session['like'])
    return redirect(redirect_url)
