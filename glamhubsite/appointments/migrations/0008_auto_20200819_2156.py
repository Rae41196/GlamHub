# Generated by Django 3.0.8 on 2020-08-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_auto_20200819_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='is_approved',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
