# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from formtest.models import Book, EBook, Impression
from formtest.forms import BookForm, EBookForm
from reportlab.pdfgen import canvas
from PIL import Image
from reportlab.lib.units import inch

def some_view(request):
    image = Image.open('/home/nagasaki/img/1680_1050_201005041215072182354.jpg')
    response = HttpResponse(content_type='application/pdf')
    response['COntent-Disposition'] = 'attachment; filename="somefilename.pdf"'
    p = canvas.Canvas(response)
    p.drawInlineImage(image,0,0,width=5*inch,height=5*inch)
    p.drawString(100, 100, u"Hello ねこworld.")
    p.showPage()
    p.save()
    return response

def book_list(request):
#    return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    books = Book.objects.filter(impressions__comment__contains="good")
    good_impressions = Impression.objects.filter(comment__contains="good")
    print(good_impressions)
    #good_impressions = books.all().impressions
    return render(request,
                  'formtest/book_list.html',     # 使用するテンプレート
                  {'books': books, 'good_impressoin': good_impressions})         # テンプレートに渡すデータ


def ebook_list(request):
#    return HttpResponse('書籍の一覧')
    ebooks = EBook.objects.all().order_by('id')
    return render(request,
                  'formtest/ebook_list.html',     # 使用するテンプレート
                  {'ebooks': ebooks})         # テンプレートに渡すデータ


def book_edit(request, book_id=None):
    """書籍の編集"""
#    return HttpResponse('書籍の編集')
    if book_id:   # book_id が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_id)
    else:         # book_id が指定されていない (追加時)
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            book = form.save(commit=False)
            book.save()
            return redirect('formtest:book_list')
    else:    # GET の時
        form = BookForm(instance=book)  # book インスタンスからフォームを作成

    return render(request, 'formtest/book_edit.html', dict(form=form, book_id=book_id))

def ebook_edit(request, ebook_id=None):
    ebook = EBook.objects.get(id=ebook_id)
    #book = Book.objects.get(id = ebook_id)
    if request.method == 'POST':
        form = EBookForm(request.POST, instance=EBook)
        if form.is_valid():
            ebook = form.save(commit=False)
            ebook.save()
            return redirect('formtest:ebook_list')
    else:
        form = EBookForm(instance=ebook)


    return render(request, 'formtest/ebook_edit.html', dict(form=form, ebook_id=ebook_id))


def book_del(request, book_id):
    """書籍の削除"""
#    return HttpResponse('書籍の削除')
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('formtest:book_list')
