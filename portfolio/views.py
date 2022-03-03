from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Album, AlbumPhoto, Category
from .forms import AlbumForm


def portfolio(request):
    """
    A view to render the portfolio page
    """
    albums = Album.objects.all()
    catg = None

    if request.GET:
        if 'category' in request.GET:
            category_key = request.GET['category']
            albums = Album.objects.filter(category__name=category_key)
            catg = Category.objects.get(name=category_key)

    page = request.GET.get('page', 1)
    paginator = Paginator(albums, 5)

    # Create pagination and define number of products per page
    # use pagination to infinite scroll
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)

    form = AlbumForm()
    if request.method == 'POST':

        album_form = AlbumForm(request.POST, request.FILES)
        if album_form.is_valid():
            album_form.save()

            album = Album.objects.get(title=request.POST['title'])

            photos = request.FILES.getlist('photos')

            photo_position = 0
            for photo in photos:

                photo_position += 1

                AlbumPhoto_line_item = AlbumPhoto(
                                        album=album,
                                        photos=photo,
                                        position=photo_position
                                    )
                AlbumPhoto_line_item.save()

    template = 'portfolio/collection.html'
    context = {
        'albums': albums,
        'catg': catg,
        'form': form,
    }

    return render(request, template, context)


def album(request, album_id):
    '''
    A view to render the album page
    '''
    album = Album.objects.get(id=album_id)

    all_photos = list()
    for ab in AlbumPhoto.objects.filter(album=album):
        photo_dict = {
            'photo': ab.photos,
            'position': ab.position
        }
        all_photos.append(photo_dict)

    photo_group = [all_photos[i:i + 10] for i in range(0, len(all_photos), 10)]

    page = request.GET.get('page', 1)
    paginator = Paginator(photo_group, 1)

    # Create pagination and define number of products per page
    # use pagination to infinite scroll
    try:
        photo_group = paginator.page(page)
    except PageNotAnInteger:
        photo_group = paginator.page(1)
    except EmptyPage:
        photo_group = paginator.page(paginator.num_pages)

    template = 'portfolio/album.html'
    context = {
        'album': album,
        'photos_gr': photo_group
    }

    return render(request, template, context)


# def portfolio(request):
#     """
#     A view to render the portfolio page
#     """
#     form = AlbumForm()
#     if request.method == 'POST':

#         album_form = AlbumForm(request.POST, request.FILES)
#         if album_form.is_valid():
#             album_form.save()

#             album = Album.objects.get(title=request.POST['title'])

#             photos = request.FILES.getlist('photos')
#             for photo in photos:
#                 AlbumPhoto_line_item = AlbumPhoto(
#                                         album=album,
#                                         photos=photo,
#                                     )
#                 AlbumPhoto_line_item.save()

#     template = 'portfolio/collection.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)
