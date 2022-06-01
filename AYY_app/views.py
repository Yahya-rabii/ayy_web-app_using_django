from ast import Not
from datetime import datetime
from multiprocessing import AuthenticationError
from urllib import response
from AYY_app import forms 
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from AYY_app.models import Product , User
from web_app.settings import SECRET_KEY
from jwt import encode


def index(request):
    return render(request, 'index.html')


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

def err_ne(request):
    return render(request, 'err_ne.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contactus(request):
    return render(request, 'contact-us.html')

def more(request):
    return render(request, 'more.html')

def false_ind(request):
    return render(request, 'false-ind.html')
    

"""  ----------------------------------------------------------------  """


def API_gl(request):
    try:
        print(dict(request.GET).get('categorie')[0])
        return JsonResponse({"status": "OK", "code": 200, "data": list(Product.objects.filter(type=dict(request.GET).get('categorie')[0]).values())})
    except:
        return JsonResponse({"status": "fuck off", "code": 200})


"""  ----------------------------------------------------------------  """


def register(request):
    if request.method == "POST":

        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            User = form.save()
            return render(request=request, template_name="index.html")
        return render(request=request, template_name="err.html")

    return render(request=request, template_name="register.html")


"""-------------------------------------------------------------------------------"""


def login(request):
    if request.method == "POST":
        form = forms.userlogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
               user = User.objects.get(email=email, password=password)
               return render (request, 'index.html')
            except:
              return render(request=request, template_name="err_ne.html")
    else:
           form = forms.userlogin()
    return render(request=request, template_name="login.html")




    #----------------------------------------------------------------#

from rest_framework.response import Response
from rest_framework.views import APIView
import datetime

from json import loads

def LoginView(request):
    request.POST = loads(request.body)
    email= request.POST['email']
    password= request.POST['password']

    if email is None:
        return Response()
    if password is None:
        return Response()

    user = User.objects.filter(email=email).first()

    if user is None:
        return JsonResponse({"status": 401, "message": "Invalid email or password"}, status=401)
        
    if user.password != password:
        return JsonResponse({"status": 401, "message": "Invalid email or password"}, status=401)


    payload={

        'id':user.id,
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=3600)

    }
           
    return JsonResponse({'message' : 'success',
                    'token': encode(payload, SECRET_KEY, algorithm='HS256')},
                    status=200)