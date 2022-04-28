''''''
import os
from django.conf import settings
from urllib.error import HTTPError
from django.shortcuts import render
from .models import Home_page_content, Instagram_mosaic
from instagrapi import Client
if os.path.exists('env.py'):
    import env


def index(request):
    """
    A view to render the index page
    """

    insta_user = os.environ.get('INSTA_USER', '')
    insta_pass = os.environ.get('INSTA_PASSWORD', '')
    no_insta = False

    # cl = Client()
    # cl.login(insta_user, insta_pass)
    # user_id = cl.user_id_from_username(insta_user)
    # medias = cl.user_medias(user_id, 1)

    # for md in medias:
    #     print(str(cl.photo_download(md.pk, 'media/home/insta/')).split("\media\home\insta\\"))

    insta_not_empty = bool(Instagram_mosaic.objects.all())

    if insta_not_empty is False:
        try:
            cl = Client()
            cl.login(insta_user, insta_pass)
            user_id = cl.user_id_from_username(insta_user)
            medias = cl.user_medias(user_id, 24)

            if len(medias):
                for media in medias:
                    if media.media_type == 1:
                        download_picture = cl.photo_download(media.pk, 'media/home/insta/')
                        picture_name = str(download_picture).split("\media\home\insta\\")
                        insta_asset = Instagram_mosaic(insta_pk=media.pk,
                                                        insta_id=media.id,
                                                        code=media.code,
                                                        taken_at=media.taken_at,
                                                        media_type=media.media_type,
                                                        picture=f'home/insta/{picture_name[1]}',
                                                        comment_count=media.comment_count,
                                                        like_count=media.like_count,
                                                        caption_text=media.caption_text,
                                                        video_url=media.video_url,
                                                        view_count=media.view_count,
                                                        video_duration=media.video_duration,
                                                        title=media.title)
                        insta_asset.save()
                no_insta = False
        except Exception:
            no_insta = False
    else:
        no_insta = False
        try:
            cl = Client()
            cl.login(insta_user, insta_pass)
            user_id = cl.user_id_from_username(insta_user)
            medias = cl.user_medias(user_id, 24)

            if len(medias):
                for media in medias:
                    if media.media_type == 1:
                        media_exists = Instagram_mosaic.objects.filter(insta_id=media.id).exists()

                        if media_exists is False:
                            download_picture = cl.photo_download(media.pk, 'media/home/insta/')
                            picture_name = str(download_picture).split("\media\home\insta\\")
                            insta_asset = Instagram_mosaic(insta_pk=media.pk,
                                                            insta_id=media.id,
                                                            code=media.code,
                                                            taken_at=media.taken_at,
                                                            media_type=media.media_type,
                                                            picture=f'home/insta/{picture_name[1]}',
                                                            comment_count=media.comment_count,
                                                            like_count=media.like_count,
                                                            caption_text=media.caption_text,
                                                            video_url=media.video_url,
                                                            view_count=media.view_count,
                                                            video_duration=media.video_duration,
                                                            title=media.title)
                            insta_asset.save()
        except Exception:
            no_insta = False

    content = Home_page_content.objects.all()

    insta_content = Instagram_mosaic.objects.all()
    all_insta_pics = list()
    for pic in insta_content:
        all_insta_pics.append(pic)
    insta_pics_group = [all_insta_pics[i:i + 8] for i in range(0, len(all_insta_pics), 8)]

    template = 'home/index.html'
    context = {
        'content': content,
        'no_insta': no_insta,
        'insta_content': insta_content,
        'insta_groups': insta_pics_group,
    }

    return render(request, template, context)
