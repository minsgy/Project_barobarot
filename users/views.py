from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
# Create your views here.

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password) 
        # 찾아서 id, paasword 일치하는 지 확인

        if user is not None:  # 값이 있을 시
            auth.login(request, user)
            return redirect('products:home')
        else:
            print('로그인 실패')
            return redirect('users:login')

    else: # 처음 접속
        return render(request, 'users/__login.html')

def userLogout(request):
    auth.logout(request)
    return redirect('products:home')

def userSignup(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                username=request.POST.get('username'), password=request.POST.get('password1'), name=request.POST.get('name'),email=request.POST.get('email'), number=request.POST.get('number')
            )
            auth.login(request, user)
            return redirect('products:home')
        print("생성안됌.")
        return redirect('users:signup')
    else:
        return render(request, 'users/__signup.html')