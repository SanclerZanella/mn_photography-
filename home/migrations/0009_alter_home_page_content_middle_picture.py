# Generated by Django 4.0 on 2021-12-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_home_page_content_middle_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_page_content',
            name='middle_picture',
            field=models.TextField(null=True),
        ),
    ]
