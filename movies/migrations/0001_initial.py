# Generated by Django 2.2.6 on 2019-11-25 00:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=400)),
                ('director', models.CharField(max_length=300)),
                ('actor', models.CharField(max_length=300)),
                ('score', models.FloatField()),
                ('rating', models.CharField(max_length=50)),
                ('audience', models.IntegerField()),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('hashtags', models.ManyToManyField(blank=True, related_name='tagged_movie', to='movies.HashTag')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
