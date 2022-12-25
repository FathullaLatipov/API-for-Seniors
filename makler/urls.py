"""makler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from rest_framework.routers import DefaultRouter

from products.views import CategoryListAPIView, AmenitiesListAPIView, HouseFavListAPIView, \
     snippet_list

from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
# router.register(r'api/v1/maklers/create', MasterAddCreateAPIView)


urlpatterns = [
    path('users/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('authorization/', include('authorization.urls')),
    path('api/v1/categories/', CategoryListAPIView.as_view()),
]

urlpatterns += doc_urls
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
