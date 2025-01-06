from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .forms import RegistrationForm
from .models import Buyer, Game, News


def platform(request):
    context = {
            'pagename': 'Главная страница',
            }
    return render(request, 'platform.html', context)


def games(request):
    context = {
            'pagename': 'Игры',
            'games':    Game.objects.all(),
            }
    return render(request, 'games.html', context)


def cart(request):
    context = {
            'pagename': 'Корзина',
            }
    return render(request, 'cart.html', context)

def news(request):
    paginator = Paginator(News.objects.all(), 3)
    page_number = request.GET.get('page', 1)
    news = paginator.get_page(page_number)
    context = {
            'pagename': 'Новости',
            'news': news,
            }
    return render(request, 'news.html', context)

def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if is_user_exist(username):
            info = {'error': f"Пользователь '{username}' уже существует"}
        elif password != repeat_password:
            info = {'error': 'Пароли не совпадают'}
        elif age < 18:
            info = {'error': 'Вы должны быть старше 18 лет'}
        else:
            Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f'Приветствуем, {username}!')

        return render(request, 'registration_page.html', {'info': info})

    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username'].strip()
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if is_user_exist(username):
                info = {'error': f"Пользователь '{username}' уже существует"}
            elif password != repeat_password:
                info = {'error': 'Пароли не совпадают'}
            elif age < 18:
                info = {'error': 'Вы должны быть старше 18 лет'}

            if not info:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')

    else:
        form = RegistrationForm()

    return render(request, 'registration_page.html', {'form': form, 'info': info})


def is_user_exist(username: str):
    if not username:
        return False
    users = Buyer.objects.all()
    for user in users:
        if user.name.strip().lower() == username.strip().lower():
            return True
    return False
