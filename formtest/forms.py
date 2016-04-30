# -*- coding: utf-8 -*-
from django.forms import ModelForm
from formtest.models import Book, EBook


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ("name", "publisher", "page",)


class EBookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = EBook
        fields = ("name", "publisher", "page", "filename",)
