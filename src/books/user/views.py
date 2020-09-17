from user.forms import UserForms
from user.models import User
from user.utils import generate_random_password

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# from faker import Faker


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
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/')
    elif request.method == 'GET':
        form = UserForms()
    context = {'user_form': form}
    return render(request, 'create_user.html', context=context)


def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForms(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/')
    elif request.method == 'GET':
        form = UserForms(instance=user)
    context = {'user_form': form}
    return render(request, 'create_user.html', context=context)
