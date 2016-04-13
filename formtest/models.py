# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django.db import models

# Create your models here.


class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"{}".format(self.name)

class EBook(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)
    filename = models.CharField('ファイル名', max_length=255)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"0.name,0.filename".format(self)

class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions')
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment

    """@property"""
    def __unicode__(self):
        return u"{}".format(self.comment)
