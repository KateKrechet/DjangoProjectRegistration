from django.shortcuts import render
from .form import Signupform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


# Create your views here.
def index(req):
    if req.user.username:
        username = req.user.first_name
        lastname = req.user.last_name
        # print(req.user.first_name, '#', req.user.id)
    else:
        username = 'Гость'
        lastname = ''
        # print(req.user.id)
    # print(req.user.username)
    data = {'username': username, 'lastname': lastname}
    return render(req, 'index.html', context=data)


def registr(req):
    print(1)
    if req.POST:
        print(2)
        anketa = Signupform(req.POST)
        if anketa.is_valid():
            print(3)
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password')
            k3 = anketa.cleaned_data.get('first_name')
            k4 = anketa.cleaned_data.get('last_name')
            k5 = anketa.cleaned_data.get('email')
            user = authenticate(username=k1, password=k2)  # сохраняет нового пользователя
            man = User.objects.get(username=k1)  # найдем нового пользователя
            # заполним поля в таблице
            man.email = k5
            man.first_name = k3
            man.last_name = k4
            man.save()
            # входим на сайт
            # login(req, user)
            return redirect('home')
    else:
        anketa = Signupform()
    data = {'regform': anketa}
    return render(req, 'registration/registration.html', context=data)
