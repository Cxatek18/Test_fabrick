from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import User
from .serializers import (
    UserSerializer,
    UserUpdateSerializer,
)


class UserCreateApiView(APIView):
    """
    Авторизация пользователя.
    """
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        request.data.copy()
        return Response(
            UserSerializer(
                request.user,
                context={"request": request}
            ).data
        )


class UserUpdateApiView(generics.UpdateAPIView):
    """
    Обновление информации пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)


class UserDeleteApiView(generics.DestroyAPIView):
    """
    Удаление пользователя.
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
