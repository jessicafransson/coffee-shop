from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """Viewing the actual shopping bag"""

    return render(request, 'bag/bag.html')
