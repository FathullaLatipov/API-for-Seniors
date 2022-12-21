from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from rest_framework.routers import DefaultRouter

from products.views import CategoryListAPIView, AmenitiesListAPIView, HouseFavListAPIView, WebAmenitiesListAPIView, \
    WebPriceListAPIView, snippet_list

from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
# router.register(r'api/v1/maklers/create', MasterAddCreateAPIView)


urlpatterns = [
    path('master/', include('masters.urls')),
    path('store/', include('store.urls')),
    path('users/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('api/v1/categories/', CategoryListAPIView.as_view()),
    path('api/v1/amenities/', AmenitiesListAPIView.as_view()),
    path('web/api/v1/web-amenities/', WebAmenitiesListAPIView.as_view()),
    path('web/api/v1/web-prices/', WebPriceListAPIView.as_view()),
    path('api/v1/fav/', HouseFavListAPIView.as_view()),

]

urlpatterns += doc_urls
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
