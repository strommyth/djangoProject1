from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewUser


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



def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if NewUser.objects.filter(id_numbers=uname).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = NewUser(id_numbers=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = NewUser.objects.filter(id_numbers=uname, password=pwd)
        if check_user:
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