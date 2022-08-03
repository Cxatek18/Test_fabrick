from rest_framework import serializers
from .models import Mailing
from user.models import (
    User
)


class MailingCreateSerializer(serializers.ModelSerializer):
    filtering_user = User.objects.all()

    class Meta:
        model = Mailing
        fields = (
            'filtering_user', 'text_to_send', 'launch_time',
            'end_time',
        )
