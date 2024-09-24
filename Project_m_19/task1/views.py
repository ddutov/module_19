from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserForm
from .models import Buyer, Game


# Create your views here.
def games_list(request):
    games = Game.objects.all()
    list_of_games = []
    i = 0
    for game in games:
        list_of_games.append(f'{game.title}' + ' | ' + f'{game.description}. ' + f'Стоимость {game.cost}')
        i += 1
    context = {
        'games': list_of_games,
    }

    return render(request, 'games.html', context)


def cart_view(request):
    return render(request, 'cart.html')


def main_page(request):
    name = 'Главная страница'

    return render(request, 'platform.html')


Buyers = Buyer.objects.all()


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        info = {}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'index.html', context={'error': info['error']})
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                print(info['error'])
                return render(request, 'index.html', context={'error': info['error']})
            for i in range(Buyer.objects.count()):
                if username == str(Buyer.objects.get(id=i+1)):
                    info['error'] = 'Пользователь уже существует'
                    print(info['error'])
                    return render(request, 'index.html', context={'error': info['error']})
            Buyer.objects.create(name=username, balance=0, age=age)
            welcome = f'Приветствуем, {username}!'
            return render(request, 'index.html', context={'welcome': welcome})
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})


def sign_up_by_html(request):
    if request.method == 'POST':
        info = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        info['username'] = username
        info['password'] = password
        info['age'] = age
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'index.html', context={'error': info['error']})
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            print(info['error'])
            return render(request, 'index.html', context={'error': info['error']})
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            print(info['error'])
            return render(request, 'index.html', context={'error': info['error']})
        users.append(info['username'])
        welcome = f'Приветствуем, {username}!'
        return render(request, 'index.html', context={'welcome': welcome})
    return render(request, 'registration_page.html')
