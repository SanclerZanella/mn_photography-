from django.db import models
import jsonfield


class Home_page_content(models.Model):
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

    carousell_photos = jsonfield.JSONField(null=True)
    middle_text = models.CharField(null=True, max_length=1000)
    middle_picture = models.TextField(null=True)
    prew_picture = models.TextField(null=True)
    w_picture = models.TextField(null=True)
    fam_picture = models.TextField(null=True)
    first_testimonial = jsonfield.JSONField(null=True)
    second_testimonial = jsonfield.JSONField(null=True)
    third_testimonial = jsonfield.JSONField(null=True)
