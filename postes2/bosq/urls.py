from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about),
    path('dashboard', views.dashboard),
    path('', views.homepage),
]