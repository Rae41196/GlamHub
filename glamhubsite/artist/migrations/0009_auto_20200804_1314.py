# Generated by Django 3.0.8 on 2020-08-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0008_auto_20200803_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistportfolio',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]