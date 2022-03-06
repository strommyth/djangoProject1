from django.shortcuts import render, redirect, get_object_or_404
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


def testdb(request):
    test2 = NewUser.objects.get(user_name__contains='陳益祥')
    test2.user_name = 'Twitter'
    test2.save()

    # 另外一種方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")
'''
def edit_member(request, user_id):
    member = get_object_or_404(NewUser, id=user_id)
    form = MemberForm(request.POST or None, instance=member)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # do something else, like redirect to a different view

    return render(request, 'MemberAdd.html', {'form': form})
'''


def mytest(request):
    return render(request, 'mytest.html')

def Vlogin(request):
    return render(request, 'Vlogin.html')