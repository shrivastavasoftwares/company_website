# Generated by Django 2.2.5 on 2021-02-09 11:43

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japhlu_app', '0004_services_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_info',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]