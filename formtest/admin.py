# -*- coding: utf-8 -*-

from django.contrib import admin
from formtest.models import Book, Impression, EBook

# Register your models here.
admin.site.register(Book)
admin.site.register(Impression)
admin.site.register(EBook)
