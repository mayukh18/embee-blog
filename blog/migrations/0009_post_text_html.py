# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_html',
            field=models.TextField(blank=True),
        ),
    ]