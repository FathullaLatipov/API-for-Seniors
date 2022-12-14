from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserProfile, UserList, UserDetailAPIView, UpdateProfileView

# router = DefaultRouter()
# router.register('api/v1/signup', UserViewSet, 'signup')

urlpatterns = [
        path('api/v1/profile/<int:pk>/', UserList.as_view()),
        path('api/v1/update-user/<int:pk>/', UpdateProfileView.as_view()),
        path('api/v1/delete-user/<int:pk>/', UserDetailAPIView.as_view()),
]
