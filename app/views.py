from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.models import Users


@csrf_exempt
def auth(request):
    if request.method == 'POST':
        users = list(Users.objects.all().values())
        login = request.POST['login']
        pas = request.POST['pass']
        for i in users:
            if login == i['login']:
                if i['password'] == pas:
                    return HttpResponse('Авторизация пройдена')
                else:
                    return HttpResponse('Неверный пароль')
        return HttpResponse('Пользователь не найден')
    return render(request, 'auth.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        users = list(Users.objects.all().values())
        login = request.POST['login']
        pas = request.POST['pass']
        for i in users:
            if login == i['login']: return HttpResponse('Пользователь уже зарегистрирован')
        user = Users()
        user.login = login
        user.password = pas
        user.save()
        return HttpResponse('Регистрация прошла успешно!')
    return render(request, 'register.html')


def index(request): return render(request, 'index.html')