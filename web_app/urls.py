import imp
from django.contrib import admin
from django.urls import path , include
from rest_framework import serializers, viewsets, routers
from AYY_app.models import User 
from AYY_app import views


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = User
            fields = ('firstname','lastname', 'email','password')
 
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users_lst', UserViewSet)


from web_app import settings

urlpatterns = [
  
    path('add_users/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

    # ----------------------------------------- 
    
    path('admin/', admin.site.urls),
    path('main/', include('AYY_app.urls')),

    # ----------------------------------------- 

    path('', views.register),
    path('user_login/', views.login),


    path('/static', include('settings.STATIC_ROOT')),  
    ]

