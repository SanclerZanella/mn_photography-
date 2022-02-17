from django.contrib import admin
from .models import Album, AlbumPhoto, Category


class AlbumPhotosAdminInline(admin.TabularInline):
    model = AlbumPhoto


class AlbumAdmin(admin.ModelAdmin):
    """
    Sort and Displays product table in Admin interface.
    """

    inlines = (AlbumPhotosAdminInline,)

    class Meta:
        model = Album

    list_display = ('category',
                    'title',
                    'date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


# Register models to construct a default form representation.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Category, CategoryAdmin)
