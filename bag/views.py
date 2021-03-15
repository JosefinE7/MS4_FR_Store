from django.shortcuts import render, get_object_or_404


def view_bag(request):
    """ A view to renders the bag contents page """

    return render(request, 'bag/bag.html')

