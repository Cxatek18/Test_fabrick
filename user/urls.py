from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
    UserCreateApiView,
    UserUpdateApiView,
    UserDeleteApiView
)

urlpatterns = [
    path('register/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('token-create/', obtain_jwt_token, name='obtain_jwt_token'),
    path('authorization/', UserCreateApiView.as_view()),
    path('update/<int:pk>/', UserUpdateApiView.as_view()),
    path('delete/<int:pk>/', UserDeleteApiView.as_view()),
]
