from django.shortcuts import render
from .models import Album, AlbumPhoto
from .forms import AlbumForm


def portfolio(request):
    """
    A view to render the portfolio page
    """
    form = AlbumForm()
    if request.method == 'POST':
        form_data = {
            'type': request.POST['type'],
            'title': request.POST['title'],
            'pre_desc': request.POST['pre_desc'],
            'date': request.POST['date'],
            'place': request.POST['place'],
            'cover': request.FILES.get('cover'),
            'description': request.POST['description'],
        }
        album_form = AlbumForm(form_data)
        if album_form.is_valid():
            album_form.save()

        album = Album.objects.get(title=request.POST['title'])

        photos = request.FILES.getlist('photos')
        for photo in photos:
            AlbumPhoto_line_item = AlbumPhoto(
                                    album=album,
                                    photos=photo,
                                   )
            AlbumPhoto_line_item.save()

    template = 'portfolio/collection.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
