from show_app.views import raiz
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.raiz),
    path('shows/new',views.new ),
    path('shows/create', views.create),
    path('shows/<int:id>', views.show_id),
    path('shows', views.shows),
    path('shows/<int:id>/edit', views.show_id_edit),
    path('shows/<int:id>/update', views.show_id_update),
    path('shows/<int:id>/destroy', views.show_id_destroy),


]
