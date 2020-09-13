# from django.shortcuts import render
from user.models import User
from user.utils import generate_random_password

from book.models import Book

from django.http import HttpResponse

from faker import Faker


def generate_password(request):

    length = int(request.GET.get('len'))
    result = generate_random_password(length)

    return HttpResponse(str(result))


def users(request):

    users = User.objects.all()
    results = ''
    for user in users:
        results += f'ID: {user.id}, Email: {user.email}'
    return HttpResponse(results)


def create_user(request):
    fake = Faker()
    user = User.objects.create(
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name()
    )
    return HttpResponse(f'ID: {user.id}, Email: {user.email}')


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
