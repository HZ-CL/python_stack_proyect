from django.urls import path
from . import views

urlpatterns = [
    path('', views.logregistro),
    path('validar', views.validar ),
    path('login', views.login),
    path('successlink', views.success),
    path('logout', views.logout)
]