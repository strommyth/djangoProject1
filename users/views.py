from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewUser
from django.contrib import auth

# Create your views here.
def home(request):
    #posts = NewUser.objects.all()
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'base.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')



def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(id_numbers = uname, password = pwd)
        # check_user = NewUser.objects.filter(id_numbers=uname, password=pwd)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')