from django.shortcuts import render
from .models import Home_page_content


def index(request):
    """
    A view to render the index page
    """

    content = Home_page_content.objects.all()
    template = 'home/index.html'
    context = {
        'content': content
    }

    return render(request, template, context)
