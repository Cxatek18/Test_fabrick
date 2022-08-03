# Generated by Django 3.2 on 2022-08-03 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_time', models.DateTimeField(blank=True, null=True, verbose_name='Время запуска')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Время окончания')),
            ],
        ),
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('Shipped', 'Отправлено'), ('Not_sent', 'Не отправлено')], default='Not_sent', max_length=120, verbose_name='Статус товара')),
                ('mailing_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailing_name', to='sender.mailing', verbose_name='Рассылка')),
                ('user_mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_mailing', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='mailing',
            name='text_to_send',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_to_send', to='sender.textmessage', verbose_name='Текст для данной рассылки'),
        ),
    ]