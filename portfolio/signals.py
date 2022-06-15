import os
import shutil
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Album, AlbumPhoto
if os.path.exists('env.py'):
    import env


@receiver(post_delete, sender=Album)
def update_albums_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Album` object is deleted.
    """

    if instance.cover:
        if 'DEVELOPMENT' in os.environ:
            if os.path.isfile(instance.cover.path):
                path_dirs = str(instance.cover.path).split(os.sep)
                del path_dirs[-1]
                shutil.rmtree("/".join(path_dirs))
        else:
            instance.cover.delete(save=False)


@receiver(post_delete, sender=AlbumPhoto)
def update_photos_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `AlbumPhoto` object is deleted.
    """

    if instance.photos:
        if 'DEVELOPMENT' in os.environ:
            if os.path.isfile(instance.photos.path):
                path_dirs = str(instance.photos.path).split(os.sep)
                del path_dirs[-1]
                folder = "/".join(path_dirs)
                number_files = len(list(file for file in os.listdir(folder)))

                if number_files > 1:
                    os.remove(instance.photos.path)
                else:
                    shutil.rmtree(folder)
        else:
            instance.photos.delete(save=False)


@receiver(pre_save, sender=Album)
def auto_delete_file_on_change_album(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Album` object is updated
    with new file.
    """

    if not instance.pk:
        return False

    try:
        old_file = Album.objects.get(pk=instance.pk).cover
    except Album.DoesNotExist:
        return False

    new_file = instance.cover

    if not old_file == new_file:
        if old_file:
            if 'DEVELOPMENT' in os.environ:
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)
            else:
                old_file.delete(save=False)
    else:
        return False


@receiver(pre_save, sender=AlbumPhoto)
def auto_delete_file_on_change_photo(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `AlbumPhoto` object is updated
    with new file.
    """

    if not instance.pk:
        return False

    try:
        old_file = AlbumPhoto.objects.get(pk=instance.pk).cover
    except AlbumPhoto.DoesNotExist:
        return False

    new_file = instance.cover

    if not old_file == new_file:
        if old_file:
            if 'DEVELOPMENT' in os.environ:
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)
            else:
                old_file.delete(save=False)
    else:
        return False
