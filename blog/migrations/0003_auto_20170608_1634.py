# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-08 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('blog', '0002_blogindexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
    ]
