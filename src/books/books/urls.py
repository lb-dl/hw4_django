# from django.contrib import admin
from user import views as uv

from book import views as bv

from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [

    path('gp/', uv.generate_password),
    path('users/', uv.users, name='users_name'),
    path('cu/', uv.create_user, name='users_create'),
    path('books/list/', bv.book_list, name='books_list'),
    path('categories/list/', bv.category_list, name='categories_list'),
    path('books/create/', bv.create_books),
    path('uu/<int:pk>/', uv.update_user, name='users_update'),
    path('cab/', bv.create_a_book, name='books_create'),
    path('uab/<int:pk>/', bv.update_a_book, name='books_update'),
    path('dab/<int:pk>/', bv.delete_a_book),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
