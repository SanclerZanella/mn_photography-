from django.contrib import admin
from .models import BioPageContent


class BioAdmin(admin.ModelAdmin):
    """
    Sort and Displays product table in Admin interface.
    """

    list_display = ('id',
                    'title')


# Register models to construct a default form representation.
admin.site.register(BioPageContent, BioAdmin)
