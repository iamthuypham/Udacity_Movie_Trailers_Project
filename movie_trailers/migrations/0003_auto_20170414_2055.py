# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-14 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_trailers', '0002_movie_trailer_youtube_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer_youtube_id',
            field=models.TextField(editable=False),
        ),
    ]