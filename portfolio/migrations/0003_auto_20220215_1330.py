# Generated by Django 3.2.7 on 2022-02-15 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_album_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='photos',
        ),
        migrations.AddField(
            model_name='album',
            name='photo',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='AlbumPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.FileField(upload_to='portfolio/album/')),
                ('album', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.album')),
            ],
        ),
    ]
