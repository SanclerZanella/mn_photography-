# Generated by Django 4.0 on 2021-12-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_home_page_content_middle_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_page_content',
            name='fam_picture',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home_page_content',
            name='prew_picture',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home_page_content',
            name='w_picture',
            field=models.TextField(null=True),
        ),
    ]
