import json
from django.core import serializers
from itertools import product
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')


def end_page(request):
    return render(request, 'end page.html')


def mysite2_bikelube(request):
    return render(request, 'site_bike_lube.html')


def mysite2_gloves(request):
    return render(request, 'site_gloves.html')


def mysite2_helmets(request):
    return render(request, 'site_helmet.html')


def mysite2_jackets(request):
    return render(request, 'site_jackets.html')


def mysite2_suit(request):
    return render(request, 'site_suit.html')


def mysite(request):
    return render(request, 'my site.html')


def mysite2_regest(request):
    return render(request, 'REGESREATION.html')


def mysite2_boots(request):
    return render(request, 'site_boots.html')


def API_gl(request):
    try:
        return JsonResponse({"status": "OK", "code": 200, "data": list(Product.objects.filter(type=dict(request.GET).get('categorie')[0]).values())})
    except:
        return JsonResponse({"status": "fuck off", "code": 200})
