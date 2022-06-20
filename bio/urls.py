from django.urls import path
from . import views


# Base url for this app and urls for other functions in this app
urlpatterns = [
    path('', views.bio, name='bio'),
    path('edit_bio/', views.edit_bio, name='edit_bio'),
]
