# Generated by Django 4.0 on 2021-12-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home_page_content',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='home_page_content',
            name='name',
        ),
        migrations.AddField(
            model_name='home_page_content',
            name='hero_caroussel',
            field=models.TextField(blank=True, null=True),
        ),
    ]