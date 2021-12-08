from django.contrib import admin
from .models import Home_page_content


class HomeAdmin(admin.ModelAdmin):
    """
    Sort and Displays product table in Admin interface.
    """

    list_display = ('carousell_photos',
                    'middle_text',
                    'middle_picture',)


# Register models to construct a default form representation.
admin.site.register(Home_page_content, HomeAdmin)
