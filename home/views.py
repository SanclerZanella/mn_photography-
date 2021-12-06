from django.shortcuts import render


def index(request):
    """
    A view to render the index page
    """
    template = 'home/index.html'

    return render(request, template)