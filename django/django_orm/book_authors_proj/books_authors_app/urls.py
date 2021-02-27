from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_books),
    path('add_book', views.add_book),
    path('view_book/<id_book>', views.book_info),
    path('view_book/asignar_autor/<id_book>', views.asignando_autor)
]