from django.shortcuts import render
from goods.models import Categories

def index(request):

    context = {
        'title': 'Суши Осака',
        'content': 'Добро пожаловать на сайт Суши Осака',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Суши Осака - О нас',
        'content':'О нас',
        'text_on_page': 'Текст о том какие мы класные'
    }

    return render(request, 'main/about.html', context)