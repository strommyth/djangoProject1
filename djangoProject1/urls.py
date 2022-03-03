from django.contrib import admin
from django.urls import path,include
import PassValue.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('PassValue/', PassValue.views.HomeView.as_view()),
]