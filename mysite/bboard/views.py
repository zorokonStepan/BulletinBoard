from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Bboard


def index(request: HttpRequest) -> HttpResponse:
    bbs = Bboard.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})
