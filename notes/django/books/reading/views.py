from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse  # import from django.http
from .models import Book


# Create your views here.
def index(request):  # creation of index view
    # return HttpResponse('Books and stuff')

    books = Book.objects.order_by('title')
    return render(request, 'reading/index.html', {'books': books})  # 'reading/index.html is the html template, books is the data


def info(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'reading/info.html', {'book': book})
