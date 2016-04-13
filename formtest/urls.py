# -*- coding: utf-8 -*-
from django.conf.urls import url
from formtest import views

urlpatterns = [
    # 書籍
    url(r'^pdf/$', views.some_view),
    url(r'^book/$', views.book_list, name='book_list'),   # 一覧
    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除
    url(r'^ebook/$', views.ebook_list, name='ebook_list'),   # 一覧
    url(r'^ebook/mod/(?P<ebook_id>\d+)/$', views.ebook_edit, name='ebook_mod'), # 修正
 ]
