from django.urls import path
from .views import (
    CreateMailerView,
    SendMessageView,
)


urlpatterns = [
    path('create-mailing/', CreateMailerView.as_view()),
    path('sender-message/', SendMessageView.as_view()),
]
