# Generated by Django 2.2.5 on 2021-02-09 11:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('japhlu_app', '0005_basic_info_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic_info',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
