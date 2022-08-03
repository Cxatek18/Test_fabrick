from django.db import models


class Mailing(models.Model):
    """
    Модель рассылки
    """
    launch_time = models.DateTimeField(
        verbose_name='Время запуска',
        null=True,
        blank=True,
    )
    text_to_send = models.CharField(
        verbose_name='Текст сообщения',
        max_length=1000,
        default='Hello, it`s text message'
    )
    end_time = models.DateTimeField(
        verbose_name='Время окончания',
        null=True,
        blank=True,
    )
    filtering_user = models.ManyToManyField(
        'user.User',
        verbose_name='Пользователи',
        related_name='filtering_user',
    )

    def __str__(self):
        return self.text_to_send

    class Meta:
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'


class TextMessage(models.Model):
    """
    Модель сообщения
    """
    STATUS_MESSAGE = [
        ('Shipped', 'Отправлено'),
        ('Not_sent', 'Не отправлено')
    ]

    user_mailing = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='user_mailing',
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    mailing_name = models.ForeignKey(
        'Mailing',
        on_delete=models.CASCADE,
        verbose_name='Рассылка',
        related_name='mailing_name',
    )
    status = models.CharField(
        verbose_name='Статус сообщения',
        choices=STATUS_MESSAGE,
        default='Not_sent',
        max_length=120,
    )

    def __str__(self):
        return f"{self.user_mailing} {self.mailing_name}"

    class Meta:
        verbose_name = 'Text message'
        verbose_name_plural = 'Texts message'
