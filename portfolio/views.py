import os
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from .models import Album, AlbumPhoto, Category
from .forms import AlbumForm, ChangePhoto
if os.path.exists('env.py'):
    import env


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

    template = 'portfolio/collection.html'
    context = {
        'albums': albums,
        'catg': catg
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
            'position': ab.pk
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


@user_passes_test(lambda u: u.is_superuser)
def create_album(request):
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
                                        photos=photo
                                       )
                AlbumPhoto_line_item.save()

            return redirect(f'/portfolio/?category={album.category}')

    template = 'portfolio/create_album.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def delete_album(request, album_pk):
    """ Delete an album """

    # Restric functionality to superuser
    if not request.user.is_superuser:
        # messages.error(request, 'Sorry, only site staff can do that.')
        return HttpResponseRedirect(request.path_info)

    # Delete chosen product from db
    album = get_object_or_404(Album, pk=album_pk)
    category = album.category
    album.delete()
    # messages.success(request, 'Product deleted!')

    return redirect(f'/portfolio/?category={category}')


@user_passes_test(lambda u: u.is_superuser)
def edit_album(request, album_pk):
    """
    A view to render the edit album form
    """
    current_album = get_object_or_404(Album, pk=album_pk)
    current_photos = list(AlbumPhoto.objects.filter(album=current_album))
    album_data = {
        'category': current_album.category,
        'title': current_album.title,
        'pre_desc': current_album.pre_desc,
        'date': current_album.date,
        'place': current_album.place,
        'cover': current_album.cover,
        'description': current_album.description,
    }
    form = AlbumForm(album_data)

    if request.method == 'POST':

        album_form = AlbumForm(request.POST, request.FILES, instance=current_album)
        if album_form.is_valid():

            album_form.save()

            album = Album.objects.get(title=request.POST['title'])

            photos = request.FILES.getlist('photos')

            for photo in photos:

                AlbumPhoto_line_item = AlbumPhoto(
                                        album=album,
                                        photos=photo
                                       )
                AlbumPhoto_line_item.save()

            return redirect(f'/portfolio/?category={album.category}')

    changePhotoForm = ChangePhoto()
    template = 'portfolio/edit_album.html'
    context = {
        'form': form,
        'changePhotoForm': changePhotoForm,
        'current_album': current_album,
        'current_photos': current_photos,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def change_photo(request, photo_pk, photo_album):
    """
    A view to render the edit album form
    """
    photoAlbum = get_object_or_404(Album, id=photo_album)
    current_photo = get_object_or_404(AlbumPhoto, pk=photo_pk, album=photoAlbum)
    folder_type = photoAlbum.category
    folder_name = photoAlbum.title
    albumPk = photoAlbum.pk

    if request.method == 'POST':
        try:
            new_file = request.FILES["photos"]
        except Exception:
            return redirect(f'/portfolio/edit_album/{albumPk}')

        old_file = current_photo.photos

        if not old_file == new_file:
            if old_file:
                if "DEVELOPMENT" in os.environ:
                    if os.path.isfile(old_file.path):
                        os.remove(old_file.path)
                else:
                    old_file.delete(save=False)
            else:
                return redirect(f'/portfolio/edit_album/{albumPk}')
        else:
            return redirect(f'/portfolio/edit_album/{albumPk}')
        
        AlbumPhoto.objects.filter(pk=photo_pk).update(photos=f'portfolio/albums/{folder_type}/{folder_name}/{new_file}')
        fs = FileSystemStorage(location=f'{settings.MEDIA_ROOT}/portfolio/albums/{folder_type}/{folder_name}')
        fs.save(new_file.name, new_file)

    return redirect(f'/portfolio/edit_album/{albumPk}')


@user_passes_test(lambda u: u.is_superuser)
def delete_photo(request, photo_pk):
    """ Delete a single photo """

    # Restric functionality to superuser
    if not request.user.is_superuser:
        # messages.error(request, 'Sorry, only site staff can do that.')
        return HttpResponseRedirect(request.path_info)

    # Delete chosen product from db
    photo = get_object_or_404(AlbumPhoto, pk=photo_pk)
    album = photo.album
    photo.delete()
    # messages.success(request, 'Product deleted!')

    return redirect(f'/portfolio/edit_album/{album.pk}')
