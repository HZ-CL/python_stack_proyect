
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('courses/destroy/<int:id>', views.destroy),
    path('courses/create', views.create),
    path('courses/destroy/confirm_delete', views.delete)
]