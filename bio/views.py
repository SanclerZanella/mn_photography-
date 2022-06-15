from django.shortcuts import render


def bio(request):
    """
    A view to render the bio page
    """

    template = 'bio/bio.html'
    context = {
    }

    return render(request, template, context)
