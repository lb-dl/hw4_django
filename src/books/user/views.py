from user.forms import UserForms
from user.models import User
from user.utils import generate_random_password

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse

# from faker import Faker


def generate_password(request):
    length = int(request.GET.get('len'))
    result = generate_random_password(length)

    return HttpResponse(str(result))


def users(request):
    users_queryset = User.objects.all().prefetch_related('books')
    context = {'user_list': users_queryset, }
    return render(request, 'list_users.html', context)


def create_user(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_name')
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
            return redirect('users_name')
    elif request.method == 'GET':
        form = UserForms(instance=user)
    context = {'user_form': form,
               'user_instance': user
               }
    return render(request, 'create_user.html', context=context)
