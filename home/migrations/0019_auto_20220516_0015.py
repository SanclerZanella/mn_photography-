# Generated by Django 3.2.7 on 2022-05-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20220514_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_page_content',
            name='first_testimonial_partner_1',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='home_page_content',
            name='first_testimonial_partner_2',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='home_page_content',
            name='second_testimonial_partner_1',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='home_page_content',
            name='second_testimonial_partner_2',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='home_page_content',
            name='third_testimonial_partner_1',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='home_page_content',
            name='third_testimonial_partner_2',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
