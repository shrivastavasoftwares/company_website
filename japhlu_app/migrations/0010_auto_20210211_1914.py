# Generated by Django 2.2.5 on 2021-02-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('japhlu_app', '0009_services_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_info',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='media/img'),
        ),
        migrations.AddField(
            model_name='basic_info',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='media/img'),
        ),
        migrations.AddField(
            model_name='basic_info',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='media/img'),
        ),
    ]