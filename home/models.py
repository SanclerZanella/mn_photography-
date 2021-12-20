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

    carousell_photo_1 = models.ImageField(null=True, blank=True,
                                          upload_to='home/carousell/')
    carousell_photo_2 = models.ImageField(null=True, blank=True,
                                          upload_to='home/carousell/')
    carousell_photo_3 = models.ImageField(null=True, blank=True,
                                          upload_to='home/carousell/')
    middle_text = models.CharField(null=True, max_length=1000)
    middle_picture = models.ImageField(null=True, blank=True,
                                       upload_to='home/middle_picture/')
    prew_picture = models.ImageField(null=True, blank=True,
                                     upload_to='home/portfolio/')
    w_picture = models.ImageField(null=True, blank=True,
                                  upload_to='home/portfolio/')
    fam_picture = models.ImageField(null=True, blank=True,
                                    upload_to='home/portfolio/')
    first_testimonial = jsonfield.JSONField(null=True)
    first_testimonial_pic = models.ImageField(null=True,
                                              blank=True,
                                              upload_to='home/testimonials/')
    second_testimonial = jsonfield.JSONField(null=True)
    second_testimonial_pic = models.ImageField(null=True,
                                               blank=True,
                                               upload_to='home/testimonials/')
    third_testimonial = jsonfield.JSONField(null=True)
    third_testimonial_pic = models.ImageField(null=True,
                                              blank=True,
                                              upload_to='home/testimonials/')
