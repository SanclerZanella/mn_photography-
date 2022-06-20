from tkinter.tix import Form
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from .models import BioPageContent
from .forms import BioForm

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


@user_passes_test(lambda u: u.is_superuser)
def edit_bio(request):
    """
    A view to render the bio page
    """
    content = BioPageContent.objects.all().first()
    current_form_data = {
                            'title': content.title,
                            'cover_picture': content.cover_picture,
                            'first_text': content.first_text,
                            'second_photo': content.second_photo,
                            'second_text': content.second_text,
                        }
    form = BioForm(current_form_data)

    if request.method == 'POST':
        form = BioForm(request.POST, request.FILES, instance=content)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(request.path_info)

    template = 'bio/bio_form.html'
    context = {
        "content": content,
        "form": form,
    }

    return render(request, template, context)
