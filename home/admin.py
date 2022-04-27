from django.contrib import admin
from .models import Home_page_content, Instagram_mosaic


class HomeAdmin(admin.ModelAdmin):
    """
    Sort and Displays product table in Admin interface.
    """

    list_display = ('id',
                    'carousell_photo_1',
                    'middle_text',
                    'middle_picture',)

class InstAdmin(admin.ModelAdmin):
    """
    Sort and Displays product table in Admin interface.
    """

    list_display = ('insta_pk',
                    'insta_id',)


# Register models to construct a default form representation.
admin.site.register(Home_page_content, HomeAdmin)
admin.site.register(Instagram_mosaic, InstAdmin)
