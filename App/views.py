from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from App.models import User


def index(request):
    return HttpResponse('啦啦啦')


class Register(TemplateView):

    template_name = 'user/register.html'

    def post(self, request):
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        email = request.POST.get('email')

        user = User()
        user.u_name = name
        user.set_pwd(pwd)
        user.u_email = email

        user.save()

        return redirect('anime78:login')


class Login(TemplateView):
    template_name = 'user/login.html'
