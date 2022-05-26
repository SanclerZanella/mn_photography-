from django.urls import path
from . import views


# Base url for this app and urls for other functions in this app
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('album/<int:album_id>', views.album, name='album'),
    path('create_album', views.create_album, name='create_album'),
    path('delete_album/<int:album_pk>', views.delete_product, name='delete_album'),
    path('edit_album/<int:album_pk>', views.edit_album, name='edit_album'),
]
