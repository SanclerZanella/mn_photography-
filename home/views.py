''''''
import os
from django.shortcuts import render
from .models import Home_page_content
from instagrapi import Client
if os.path.exists('env.py'):
    import env


def index(request):
    """
    A view to render the index page
    """

    insta_user = os.environ.get('INSTA_USER', '')
    insta_pass = os.environ.get('INSTA_PASSWORD', '')

    cl = Client()
    cl.login(insta_user, insta_pass)
    user_id = cl.user_id_from_username("sancler_z")
    medias = cl.user_medias(user_id)

    print(len(medias))

    content = Home_page_content.objects.all()
    template = 'home/index.html'
    context = {
        'content': content
    }

    return render(request, template, context)
