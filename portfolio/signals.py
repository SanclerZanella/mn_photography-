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
                shutil.rmtree("/".join(path_dirs))
        else:
            instance.photos.delete(save=False)


# @receiver(pre_save, sender=Album)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `Home_page_content` object is updated
#     with new file.
#     """

#     old_files = {
#     'carousell_photo_1': Home_page_content.objects.get(pk=instance.pk).carousell_photo_1,
#     'carousell_photo_2':Home_page_content.objects.get(pk=instance.pk).carousell_photo_2,
#     'carousell_photo_3':Home_page_content.objects.get(pk=instance.pk).carousell_photo_3,
#     'middle_picture':Home_page_content.objects.get(pk=instance.pk).middle_picture,
#     'prew_picture':Home_page_content.objects.get(pk=instance.pk).prew_picture,
#     'w_picture':Home_page_content.objects.get(pk=instance.pk).w_picture,
#     'fam_picture':Home_page_content.objects.get(pk=instance.pk).fam_picture,
#     'first_testimonial_pic':Home_page_content.objects.get(pk=instance.pk).first_testimonial_pic,
#     'second_testimonial_pic':Home_page_content.objects.get(pk=instance.pk).second_testimonial_pic,
#     'third_testimonial_pic':Home_page_content.objects.get(pk=instance.pk).third_testimonial_pic
#     }

#     new_files = {
#         'carousell_photo_1': instance.carousell_photo_1,
#         'carousell_photo_2':instance.carousell_photo_2,
#         'carousell_photo_3':instance.carousell_photo_3,
#         'middle_picture':instance.middle_picture,
#         'prew_picture':instance.prew_picture,
#         'w_picture':instance.w_picture,
#         'fam_picture':instance.fam_picture,
#         'first_testimonial_pic':instance.first_testimonial_pic,
#         'second_testimonial_pic':instance.second_testimonial_pic,
#         'third_testimonial_pic':instance.third_testimonial_pic
#     }

#     for key, item in old_files.items():
#         try:
#             item
#         except Home_page_content.DoesNotExist:
#             return False

#         if not item == new_files[key]:
#             if item:
#                 if 'DEVELOPMENT' in os.environ:
#                     if os.path.isfile(item.path):
#                         os.remove(item.path)
#                     else:
#                         item.delete(save=False)
#         else:
#             return False
