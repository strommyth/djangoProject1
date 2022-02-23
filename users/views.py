from django.shortcuts import render
from .models import NewUser
# Create your views here.

def index(request):
    posts = NewUser.objects.all()
    return render(request, 'index.html',{"posts": posts})