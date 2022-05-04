"""web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pickle import FRAME
from django.contrib import admin
from django.urls import path , include


from rest_framework import serializers, viewsets, routers
from AYY_app.models import User 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = User
            #exclude = ('firstname',)
            fields = ('url', 'firstname','lastname','password', 'email')
            write_only_fields =  ('password',)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users_lst', UserViewSet)


from AYY_app import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  
    path('add_users/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

    # ----------------------------------------- 
    
    path('admin/', admin.site.urls),
    path('main/', include('AYY_app.urls')),
    path('user_regest/', views.register),


    
    ]

