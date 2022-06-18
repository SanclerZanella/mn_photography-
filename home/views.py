''''''
import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from .models import Home_page_content, Instagram_mosaic
from .forms import IndexForm
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
        except Exception as ext:
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

@user_passes_test(lambda u: u.is_superuser)
def edit_index(request, db_id):
    """
    A view to render the index page edit form
    """
    current_page_content = Home_page_content.objects.all().first()

    current_form_data = {
                            'carousell_photo_1': current_page_content.carousell_photo_1,
                            'carousell_photo_2': current_page_content.carousell_photo_2,
                            'carousell_photo_3': current_page_content.carousell_photo_3,
                            'middle_text': current_page_content.middle_text,
                            'middle_picture': current_page_content.middle_picture,
                            'prew_picture': current_page_content.prew_picture,
                            'w_picture': current_page_content.w_picture,
                            'fam_picture': current_page_content.fam_picture,
                            'first_testimonial_pic': current_page_content.first_testimonial_pic,
                            'first_testimonial_text': current_page_content.first_testimonial_text,
                            'first_testimonial_partner_1': current_page_content.first_testimonial_partner_1,
                            'first_testimonial_partner_2': current_page_content.first_testimonial_partner_2,
                            'second_testimonial_pic': current_page_content.second_testimonial_pic,
                            'second_testimonial_text': current_page_content.second_testimonial_text,
                            'second_testimonial_partner_1': current_page_content.second_testimonial_partner_1,
                            'second_testimonial_partner_2': current_page_content.second_testimonial_partner_2,
                            'third_testimonial_pic': current_page_content.third_testimonial_pic,
                            'third_testimonial_text': current_page_content.third_testimonial_text,
                            'third_testimonial_partner_1': current_page_content.third_testimonial_partner_1,
                            'third_testimonial_partner_2': current_page_content.third_testimonial_partner_2,
                        }
    form = IndexForm(current_form_data)

    if request.method == 'POST':
        form = IndexForm(request.POST, request.FILES, instance=current_page_content)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(request.path_info)

    template = 'home/index_form.html'
    context = {
        'form': form,
        'content_id': db_id,
        'current_content': current_page_content,
    }

    return render(request, template, context)
