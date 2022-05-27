from django.db import models


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

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(null=True, max_length=150)
    pre_desc = models.CharField(null=True, max_length=500)
    date = models.DateField(null=True)
    place = models.CharField(null=True, max_length=500)
    cover = models.ImageField(blank=True, null=True, upload_to="portfolio/covers/")
    description = models.TextField(null=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        album_type = self.category.name
        folder_type = album_type.replace(" ", "_")
        album_title = self.title
        folder_name = album_title.replace(" ", "_")

        for field in self._meta.fields:
            if field.name == 'cover':
                field.upload_to = f"portfolio/covers/{folder_type}/{folder_name}"
        super(Album, self).save()

    def __str__(self):
        return self.title


class AlbumPhoto(models.Model):
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

    album = models.ForeignKey(Album, default=None, on_delete=models.CASCADE, related_name='lineitems')
    photos = models.ImageField(upload_to="portfolio/albums/")

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        album_type = self.album.category.name
        folder_type = album_type.replace(" ", "_")
        album_title = self.album.title
        folder_name = album_title.replace(" ", "_")

        for field in self._meta.fields:
            if field.name == 'photos':
                field.upload_to = f"portfolio/albums/{folder_type}/{folder_name}"
        super(AlbumPhoto, self).save()

    def __str__(self):
        return self.album.title


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
