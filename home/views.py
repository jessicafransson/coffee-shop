from django.shortcuts import render


# Create your views here.
def index(request):
    """
    A view to return to home page
    """
    return render(request, 'home/index.html')


def privacy(request):
    """
    A view to the privacy page
    """
    return render(request, "home/privacy.html")


def terms(request):
    """
    A view to terms page
    """
    return render(request, "home/terms.html")


def delivery(request):
    """
    A view to the delivery page
    """
    return render(request, "home/delivery.html")
