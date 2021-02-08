# Generated by Django 2.2.5 on 2021-02-05 15:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=100, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True)),
            ],
        ),
    ]
