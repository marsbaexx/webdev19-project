from django.shortcuts import render

# Create your views here.
from .models import Found, Author, HelpInfo, HelpType


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Found.objects.all().count()
    num_instances = HelpInfo.objects.all().count()
    # статус запроса (статус = 'a')
    num_instances_available = HelpInfo.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_founder': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


return render(
    request,
    'index.html',
     context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
)