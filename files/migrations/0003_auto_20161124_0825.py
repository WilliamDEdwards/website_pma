# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 08:25


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20160726_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='download',
            name='md5',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='md5',
        ),
    ]
