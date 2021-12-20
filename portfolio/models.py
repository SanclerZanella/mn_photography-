from django.db import models
import jsonfield


class Album(models.Model):
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

    type = models.CharField(null=True, max_length=25)
    title = models.CharField(null=True, max_length=150)
    pre_desc = models.CharField(null=True, max_length=500)
    date = models.DateField(null=True)
    place = models.CharField(null=True, max_length=500)
    cover = jsonfield.JSONField(null=True)
    description = models.TextField(null=True)
    photos = jsonfield.JSONField(null=True)
