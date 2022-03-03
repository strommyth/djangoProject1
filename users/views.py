from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewUser
from django.contrib import auth

# Create your views here.
def home(request):
    #posts = NewUser.objects.all()
    if 'user' in request.session:
        current_user = request.session['user']
        user_test = request.user.user_name
        user_list = NewUser.objects.all()
        print(user_list)
        #username = NewUser.objects.get(user_name=request.user.user_name)
        #userprofile = NewUser.objects.get(username=username)
        param = {'current_user': current_user, 'user_test':user_test, 'user_list':user_list,}
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

def SEC_303(request):
    if 'user' in request.session:
        user_test = NewUser.objects.all()
        #username = NewUser.objects.get(user_name=request.user.user_name)
        #userprofile = NewUser.objects.get(username=username)
        param = {'user_test':user_test}
        return render(request, 'SEC303.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')

def SEC_404(request):
    if 'user' in request.session:
        user_test = NewUser.objects.all()
        #username = NewUser.objects.get(user_name=request.user.user_name)
        #userprofile = NewUser.objects.get(username=username)
        param = {'user_test':user_test}
        return render(request, 'SEC404.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')