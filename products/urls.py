from django.urls import path
from rest_framework.routers import DefaultRouter
from products.views import HouseDetailAPIView, HouseAddCreateAPIView, \
    HouseUpdateAPIView, HouseDestroyAPIView, WebHomeCreateView, WebHomeListAPIView, \
    SearchWebHomeListAPIView, WishlistHouseDetailAPIView, UserWishlistModelView, \
    GetHouseFavListAPIView, RandomHouseModelAPIView
router = DefaultRouter()
router.register(r'api/v1/houses/wishlist-products', UserWishlistModelView)
router.register(r'api/v1/houses/delete', HouseDestroyAPIView)
router.register(r'web/api/v1/products/create', WebHomeCreateView)

urlpatterns = [
    path('web/api/v1/products/', WebHomeListAPIView.as_view()),
    path('api/v1/products/updates/<int:pk>', HouseUpdateAPIView.as_view()),
    path('web/api/v1/products/popular', RandomHouseModelAPIView.as_view()),
    path('web/api/v1/products/search/', SearchWebHomeListAPIView.as_view()),
    path('api/v1/houses/get-wishlist-products', GetHouseFavListAPIView.as_view()),
    path('web/api/v1/products/<int:pk>', HouseDetailAPIView.as_view()),
]

urlpatterns += router.urls
