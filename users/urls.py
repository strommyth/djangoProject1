from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('SEC303/', views.SEC_303, name='SEC303'),
    path('SEC404/', views.SEC_404, name='SEC404'),
    path('testdb/', views.testdb, name='testdb'),
   # path('MemberAdd/', views.edit_member(), name='MemberAdd'),
    path('mytest/', views.mytest, name='mytest'),
    path('Vlogin/', views.Vlogin, name='Vlogin'),

]