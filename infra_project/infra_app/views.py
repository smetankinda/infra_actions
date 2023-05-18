from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Даже получилось изменить фразу!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
