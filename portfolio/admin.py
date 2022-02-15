from django.contrib import admin
from .models import Album, AlbumPhoto


class AlbumPhotosAdminInline(admin.TabularInline):
    model = AlbumPhoto


class AlbumAdmin(admin.ModelAdmin):
    """
    Sort and Displays product table in Admin interface.
    """

    inlines = (AlbumPhotosAdminInline,)

    class Meta:
        model = Album

    list_display = ('type',
                    'title',
                    'date',)


# Register models to construct a default form representation.
admin.site.register(Album, AlbumAdmin)
