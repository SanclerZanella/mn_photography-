import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import BioPageContent
if os.path.exists('env.py'):
    import env


@receiver(post_delete, sender=BioPageContent)
def update_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `BioPageContent` object is deleted.
    """

    old_files = {
        'cover_picture': instance.cover_picture,
        'second_photo':instance.second_photo
    }

    for key, item in old_files.items():
        if item:
            if 'DEVELOPMENT' in os.environ:
                if os.path.isfile(item.path):
                    os.remove(item.path)
            else:
                item.delete(save=False)


@receiver(pre_save, sender=BioPageContent)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `BioPageContent` object is updated
    with new file.
    """

    old_files = {
    'cover_picture': BioPageContent.objects.get(pk=instance.pk).cover_picture,
    'second_photo':BioPageContent.objects.get(pk=instance.pk).second_photo
    }

    new_files = {
        'cover_picture': instance.cover_picture,
        'second_photo':instance.second_photo
    }

    for key, item in old_files.items():
        try:
            item
        except BioPageContent.DoesNotExist:
            return False

        if not item == new_files[key]:
            if item:
                if 'DEVELOPMENT' in os.environ:
                    if os.path.isfile(item.path):
                        os.remove(item.path)
                    else:
                        item.delete(save=False)
