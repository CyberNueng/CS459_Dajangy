"""hw01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from rent import views
from rent.serializers import routers

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'car', views.CarViewSet)
router.register(r'rent', views.RentViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    url('admin/', admin.site.urls),
    url('oauth/', include('social_django.urls', namespace='social')),
    #url('list/', views.CarListView.as_view(), name='carlist'),
    url('', views.HomeView.as_view(), name='home')
]
