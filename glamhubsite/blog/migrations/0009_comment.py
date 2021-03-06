# Generated by Django 3.0.8 on 2020-08-05 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200804_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(help_text='Your name', max_length=80)),
                ('email', models.EmailField(blank=True, help_text='Your Email', max_length=254)),
                ('body', models.TextField(help_text='Your comment')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.BlogPost')),
            ],
            options={
                'ordering': ['created_on', 'participant_name'],
            },
        ),
    ]
