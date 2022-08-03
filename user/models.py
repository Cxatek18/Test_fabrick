from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель Юзера или клиента
    """
    GENDER = [
        ('Man', 'Мужчина'),
        ('Women', 'Женщина'),
        ('Indefinite', 'Неопределенно'),
    ]

    username = models.CharField(
        verbose_name='Логин пользователя', max_length=50,
        unique=True,
    )
    slug = AutoSlugField(
        populate_from='username'
    )
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(
        verbose_name='Номер телефона пользователя', unique=True,
        null=True, blank=True
    )
    code_mobile_operator = models.CharField(
        verbose_name='Код оператора',
        max_length=5,
        null=True, blank=True
    )
    time_zone = models.CharField(
        verbose_name='Временная зона',
        max_length=255,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )
    gender_user = models.CharField(
        verbose_name='Пол',
        choices=GENDER,
        default='Indefinite',
        max_length=120,
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Является админом'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Является активным'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.code_mobile_operator = str(self.phone_number)[2:5]
        self.time_zone = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_slug': self.slug})

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
