# Generated by Django 4.0 on 2021-12-08 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_home_page_content_hero_caroussel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home_page_content',
            old_name='hero_caroussel',
            new_name='content',
        ),
    ]
