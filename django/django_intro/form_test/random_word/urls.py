from django.urls import path
from . import views

urlpatterns = [
    path('random_word/', views.pag),
    path('random_word/generated', views.random_pag),
    path('random_word/random_reset', views.reset)
]