# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formtest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u66f8\u7c4d\u540d')),
                ('publisher', models.CharField(blank=True, max_length=255, verbose_name='\u51fa\u7248\u793e')),
                ('page', models.IntegerField(blank=True, default=0, verbose_name='\u30da\u30fc\u30b8\u6570')),
                ('filename', models.CharField(max_length=255, verbose_name='\u30d5\u30a1\u30a4\u30eb\u540d')),
            ],
        ),
    ]