from django.shortcuts import render, get_object_or_404

def view_likes(request):
    """ A view to renders the likes contents page """

    return render(request, 'likes/likes.html')

