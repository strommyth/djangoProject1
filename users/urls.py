from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('SEC303/', views.SEC_303, name='SEC303'),
    path('SEC404/', views.SEC_404, name='SEC404'),
]