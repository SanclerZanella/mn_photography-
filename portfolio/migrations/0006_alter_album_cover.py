# Generated by Django 3.2.7 on 2022-02-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_rename_albumphotos_albumphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/album/'),
        ),
    ]
