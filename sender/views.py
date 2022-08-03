from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    MailingCreateSerializer
)
from .models import (
    Mailing
)
from .services.sender_message import (
    SenderMessage
)


class CreateMailerView(generics.CreateAPIView):
    """
    Создание новой рассылки
    """
    serializer_class = MailingCreateSerializer
    model = Mailing


class SendMessageView(APIView):
    """
    Рассылка сообщений
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        mailing_id = request.data.get('mailing_id')
        mailing_obj = Mailing.objects.get(id=mailing_id)
        user_in_mailing = mailing_obj.filtering_user.all()
        text_message = mailing_obj.text_to_send
        sender = SenderMessage(
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\
            .eyJleHAiOjE2OTA5NzQ5MzIsImlzc\
            yI6ImZhYnJpcXVlIiwibmFtZSI6IktpbGFuaXMxOCJ9.\
            MLA2RyzmjIBUYttgGml-q-QVJMe_49yYzXx8JKBowuk',
        )
        for user in user_in_mailing:
            print(user)
            sender.send(user.id, user.phone_number, text_message)
        return Response('ok')
