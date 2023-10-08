from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Bboard


def index(request: HttpRequest):
    title = 'Список объявлений\r\n\r\n\r\n'

    data = [title]
    for bb in Bboard.objects.order_by('-published'):
        data.append(f'{bb.title}\r\n{bb.content}\r\n\r\n')
    return HttpResponse(''.join(data), content_type='text/plain; charset=utf-8')

