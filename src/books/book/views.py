from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from book.models import Book
from faker import Faker


def create_books(request):
    fake = Faker()
    book = Book.objects.create(
        author=fake.first_name(),
        title=fake.last_name()
    )
    return HttpResponse(f'Author: {book.author}, title: {book.title}')


def book_list(request):
    all_books = Book.objects.all()
    results = ''
    for book in all_books:
        results += f'Author: {book.author}, title: {book.title}'
    return HttpResponse(results)

def create_a_book(request):

    return HttpResponse('Creat a new book')