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
    cover = models.ImageField(blank=True, null=True,
                              upload_to='portfolio/covers/')
    description = models.TextField(null=True)

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

    album = models.ForeignKey(Album, default=None, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to="portfolio/albums/")

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        album_type = self.album.type
        folder_type = album_type.replace(" ", "_")
        album_title = self.album.title
        folder_name = album_title.replace(" ", "_")

        for field in self._meta.fields:
            if field.name == 'photos':
                field.upload_to = f"portfolio/albums/{folder_type}/{folder_name}"
        super(AlbumPhoto, self).save()

    def __str__(self):
        return self.album.title
