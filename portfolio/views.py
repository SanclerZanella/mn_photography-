from django.shortcuts import render


def portfolio(request):
    """
    A view to render the portfolio page
    """
    template = 'portfolio/collection.html'
    context = {
    }

    return render(request, template, context)
