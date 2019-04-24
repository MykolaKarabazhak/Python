from django.conf import settings
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import path
from random import choices, randrange
from django.http import HttpResponse
import re
import string
cortej_contol = ("http", "https", "ftp")


# Задание 3. URL shortener
#
# Реализуйте сервис для сокращения ссылок. Примеры таких сервисов:
#  , http://t.co, http://goo.gl
# Пример ссылки: http://bit.ly/1qJYR0y
#
# Вам понадобится шаблон с формой для отправки ссылки (файл index.html),
# и две функции, одна для обработки запросов GET и POST для сабмита URL
# и отображения результата, и вторая для редиректа с короткого URL на исходный.
# Для хранения соответствий наших коротких ключей и полных URL мы будем
# использовать кеш Django, django.core.cache
# Экземпляр cache уже импортирован, и используется следующим образом.
# Сохранить значение:
#
#  cache.add(key, value)
#
# Извлечь значение:
#
#  cache.get(key, default_value)
#
# Второй аргумент метода get - значение по умолчанию,
# если ключ не найден в кеше.
#
# Вы можете запустить сервер для разработки, и посмотреть
# ответы ваших функций в браузере:
#
# python homework03.py runserver


# Конфигурация, не нужно редактировать
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['']
        }]
    )
def random_key():
    """
    Случайный короткий ключ, состоящий из цифр и букв.
    Минимальная длина ключа - 5 символов. Для генерации случайных
    последовательностей вы можете воспользоваться библиотекой random.
    """
    #сделал так решил не тянуть лишние библиотеки 
    return ''.join(choices(string.ascii_letters + string.digits, k=randrange(5,8)))

def index(request):
    """
    При запросе методом GET, отдаем HTML страницу (шаблон index.html) с формой
    с одним полем url типа text (отредактируйте шаблон, дополните форму).

    При отправке формы методом POST извлекаем url из request.POST и
    делаем следующее:

    1. Проверяем URL. Допускаются следующие схемы: http, https, ftp

    Если URL не прошел проверку - отобразите на нашей странице с формой
    сообщение о том, какие схемы поддерживаются.

    Если URL прошел проверку:

    2. Создаем случайный короткий ключ, состоящий из цифр и букв
    (функция random_key).

    3. Сохраняем URL в кеш со сгенерированным ключом:

    cache.add(key, url)

    4. Отдаем ту же страницу с формой и дополнительно отображаем на ней
    кликабельную короткую ссылку (HTML тег 'a') вида
    http://localhost:8000/<key>
    """
    if "url" in request.POST:
        return check_post(request)
    else:
        return render(request,"index.html")
    
def check_post(request):
    """ function make check url(http,https,ftp)"""
    url = request.POST['url']
    for i in cortej_contol:
        if url[:3] == i or url[:4] == i or url[:5] == i:
            key_random = random_key()
            click = 0 
            cache.add(url,[key_random,click])
            short_url = "http://127.0.0.1:8000/" + key_random 
            return render(request, "index1.html", {
                    "url": short_url, 
                    "key" : key_random
                    })
 
    else:
        return render(request,"index1.html" , {
                    "fell":"недопустимое имя URL",
                    "inf": "Должно начинаться с Http,Https,Ftp"
                    })


def redirect_view(request, key):
    """
    Функция обрабатывает сокращенный URL вида http://localhost:8000/<key>
    Ищем ключ в кеше (cache.get). Если ключ не найден,
    редиректим на главную страницу (/). Если найден,
    редиректим на полный URL, сохраненный под данным ключом.
    """
    if request.method == 'GET':
        if cache.get(key):
            value_key = cache.get(key)
            cache.delete(key)
            value_key[1] += 1
            cache.add(key_random, [value_key[0], value_key[1]])
            return redirect(to=ch[0])
        else:
            return redirect(to='/')
    


def stats(request, key):
    """
    Статистика кликов на сокращенные ссылки.
    В теле ответа функция возращает количество
    переходов по данному коду.
    """
    if request.method == "GET":
        click = cache.get(key)
        return HttpResponse(click[1])
    else:
        return render(request,"index1.html", {
            "no_key":"Такого ключа нет"
            })


urlpatterns = [
    path('', index),
    path(r'stats/<key>', stats),
    path(r'<key>', redirect_view),
    path(r'stats/', index),
]


if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
