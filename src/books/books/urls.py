"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
# from user import views as uv
# from django.contrib import admin
from user import views as uv

from django.urls import path

urlpatterns = {

    path('gp/', uv.generate_password),
    path('users/', uv.users),
    path('cu/', uv.create_user),
    path('books/list/', uv.book_list),
    path('books/create/', uv.create_books),
}
