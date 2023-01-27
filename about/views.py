from django.shortcuts import render

# Create your views here.


def view_about_page(request):
    """ A view to return the about us page """

    return render(request, 'about/about.html')
