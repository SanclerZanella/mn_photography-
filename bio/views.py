from django.shortcuts import render
from .models import BioPageContent

def bio(request):
    """
    A view to render the bio page
    """
    content = BioPageContent.objects.all().first()

    template = 'bio/bio.html'
    context = {
        "content": content,
    }

    return render(request, template, context)
