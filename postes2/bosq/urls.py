from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about),
    path('dashboard', views.dashboard),
    # path('login', views.login),
    path('', views.homepage), 
    path('login', views.login, name='login'), # login
    path('karyawan', views.karyawan_index, name='karyawan_index'), # Read
    path('karyawan/create/', views.karyawan_create, name='karyawan_create'),# Create
    path('karyawan/update/<int:karyawan_id>/', views.karyawan_update, name='karyawan_update'),
    path('karyawan/delete/<int:karyawan_id>', views.karyawan_delete, name='karyawan_delete'),
     
]