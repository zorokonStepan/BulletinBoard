from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

from .models import Bboard


def index(request: HttpRequest):
    template = loader.get_template('bboard/index.html')
    bbs = Bboard.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
