# Generated by Django 3.0.8 on 2020-08-03 11:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_name', models.CharField(max_length=255)),
                ('message', ckeditor_uploader.fields.RichTextUploadingField(max_length=5000)),
                ('message_email', models.EmailField(max_length=70)),
            ],
        ),
    ]
