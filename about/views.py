from django.shortcuts import render


def view_about_page(request):
    """ A view to return the about us page """

    return render(request, 'about/about.html')


def view_farm_page(request):
    """A view to the about us and our farm page"""

    return render(request, 'about/farm.html')


def view_flavours_page(request):
    """A View to the about us and flavours page"""

    return render(request, 'about/flavours.html')
