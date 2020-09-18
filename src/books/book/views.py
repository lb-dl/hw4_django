from book.forms import BookForms
from book.models import Book

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

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
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/list/')
    elif request.method == 'GET':
        form = BookForms()
    context = {'book_form': form}
    return render(request, 'create_book.html', context=context)


def update_a_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForms(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/list/')
    elif request.method == 'GET':
        form = BookForms(instance=book)
    context = {'book_form': form}
    return render(request, 'create_book.html', context=context)


def delete_a_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book:
        Book.objects.get(pk=pk).delete()
        return HttpResponse(f'Author: {book.author}, title: {book.title}, year: {book.year}, was successfully deleted')
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/list/')
    elif request.method == 'GET':
        form = BookForms()
    context = {'book_form': form}
    return render(request, 'create_book.html', context=context)
