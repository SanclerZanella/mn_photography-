from django.urls import path
from . import views


# Base url for this app and urls for other functions in this app
urlpatterns = [
    path('', views.index, name='home'),
    path('edit_index/<db_id>', views.edit_index, name='edit_index'),
]
