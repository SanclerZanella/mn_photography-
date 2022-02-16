from django.shortcuts import render
from .models import Album, AlbumPhoto
from .forms import AlbumForm


def portfolio(request):
    """
    A view to render the portfolio page
    """
    form = AlbumForm()
    if request.method == 'POST':

        album_form = AlbumForm(request.POST, request.FILES)
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
