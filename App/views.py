from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, DetailView

from App.models import User
from . import models


def index(request):
    return HttpResponse('啦啦啦')


class Register(TemplateView):

    template_name = 'user/register.html'

    def post(self, request):
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        user = User()
        user.u_name = name
        user.set_pwd(pwd)
        user.u_email = email
        user.u_icon = icon

        user.save()

        return redirect(reverse('78anime:login'))


class Login(TemplateView):
    template_name = 'user/login.html'

    def post(self, request):
        name = request.POST.get('name')
        pwd = request.POST.get('password')

        try:
            user = User.objects.get(pk=name)
            if user.check_pwd(pwd):
                request.session['username'] = name
                return redirect(reverse('78anime:index'))
            else:
                request.session['msg'] = '用户名或密码错误'
                return redirect(reverse('78anime:login'))
        except:
            request.session['msg'] = '用户不存在'
            return redirect(reverse('78anime:login'))


class UserInfo(DetailView):
    template_name = 'user/userinfo.html'

    model = User
