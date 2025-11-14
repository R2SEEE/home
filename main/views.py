from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    content = {
        'content': 'Магазин Lost|Home',
    }
    return render(request, 'main/index.html', context=content)


def about(request):
    content = {
        'content': 'Магазин Lost|Home',
        'text_on_page': 'Будет инофрмация о магазине',
    }
    return render(request, 'main/about.html', context=content)
