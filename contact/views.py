from django.shortcuts import render


def contact(request):
    """
    A view to render the contact page
    """

    template = 'contact/contact.html'
    context = {
    }

    return render(request, template, context)
