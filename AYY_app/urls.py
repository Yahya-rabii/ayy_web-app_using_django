from django.urls import path
from . import views


urlpatterns = [

    path('', views.index),
    path('mysite', views.mysite),
    path('gloves', views.mysite2_gloves),
    path('bikelube', views.mysite2_bikelube),
    path('jackets', views.mysite2_jackets),
    path('suit', views.mysite2_suit),
    path('boots', views.mysite2_boots),
    path('helmets', views.mysite2_helmets, name='helmets'),
    path('regest', views.mysite2_regest),
    path('end_page', views.end_page),



    path('api_gl', views.API_gl),




]