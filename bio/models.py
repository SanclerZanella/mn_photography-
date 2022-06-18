from msilib.schema import Class
from django.db import models


class BioPageContent(models.Model):
    """
    Category Model
    Attributes:
        *name: A string indicating the category name;
        *friendly_name: A string indicating category friendly name.
    Sub-classes:
        *Meta: Display the object's plural name.
    Methods:
        *__str__: Display the object's headline in the admin interface,
                  it returns a nice, human-readable representation of
                  the model;
        *get_friendly_name: Display the object's friendly name.
    """

    title = models.CharField(null=True, max_length=1000)
    cover_picture = models.ImageField(null=True, blank=True, upload_to='bio/cover/')
    first_text = models.TextField(null=True, max_length=1000)
    second_photo = models.ImageField(null=True, blank=True, upload_to='bio/second/')
    second_text = models.TextField(null=True, max_length=1000)
