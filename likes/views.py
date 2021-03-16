from django.shortcuts import render, redirect


def view_likes(request):
    """ A view to renders the likes contents page """

    return render(request, 'likes/likes.html')


def add_to_likes(request, item_id):
    """ Add a product to the likes category """

    redirect_url = request.POST.get('redirect_url')
    likes = request.session.get('likes', {})

    request.session['likes'] = likes
    print(request.session['likes'])
    return redirect(redirect_url)
