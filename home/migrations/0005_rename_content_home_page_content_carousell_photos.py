# Generated by Django 4.0 on 2021-12-08 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_hero_caroussel_home_page_content_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home_page_content',
            old_name='content',
            new_name='carousell_photos',
        ),
    ]