from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, RegForm
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib import auth
from django.urls import reverse

# Create your views here.
@csrf_exempt
def login(request):
    # POST步骤：获取用户提交的表单的信息
    if request.POST.get('flag') == 'login':
        password = request.POST.get('password')
        username = request.POST.get('username')
        data = {}
        try:
            user = User.objects.get(username=username)
        except:
            data['status'] = 'user'
            return JsonResponse(data)
        pwd = user.password
        if check_password(password, pwd):
            auth.login(request, user)
            data['status'] = 'success'
            return JsonResponse(data)
        else:
            data['status'] = 'password'
            return JsonResponse(data)
    # GET步骤：就是获取页面，表单为空
    else:
        context = {}
        return render(request, 'login.html', context)
    

@csrf_exempt
def register(request):
    # POST步骤：获取用户提交的表单的信息
    if request.POST.get('flag') == 'register':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = User.objects.create_user(username, email, password)   # 在数据库中注册user
        user.save()
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        data = {}
        data['status'] = 'success'
        return JsonResponse(data)
    elif request.POST.get('flag') == 'get_info':
        user_all = User.objects.all()
        username = []
        email = []
        for i in user_all:
            username.append(i.username)
            email.append(i.email)

        context = {
            'username': username,
            'email': email,
        }
        return JsonResponse(context)
    

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('next', reverse('home')))
