import imp
from types import GenericAlias
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



def mysite2_boots(request):
    return render(request, 'site_boots.html')



def err_v(request):
    return render(request, 'err.html')
"""  ----------------------------------------------------------------  """



def API_gl(request):
    try:
        print(dict(request.GET).get('categorie')[0])
        return JsonResponse({"status": "OK", "code": 200, "data": list(Product.objects.filter(type=dict(request.GET).get('categorie')[0]).values())})
    except:
        return JsonResponse({"status": "fuck off", "code": 200})





"""  ----------------------------------------------------------------  """

from django.shortcuts import  render
from .forms import NewUserForm


def register(request):
	if request.method == "POST":
	
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return render (request=request, template_name="index.html")
		return render (request=request, template_name="err.html")

	return render (request=request, template_name="register.html")

"""-------------------------------------------------------------------------------"""