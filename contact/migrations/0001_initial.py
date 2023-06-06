# Generated by Django 4.2.1 on 2023-06-06 12:01

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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_first', models.CharField(max_length=45, verbose_name='Первый номер телефона')),
                ('phone_number_second', models.CharField(blank=True, max_length=45, null=True, verbose_name='Второй номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('hour_working', models.CharField(max_length=200, verbose_name='Время работы')),
                ('city', models.CharField(max_length=250, verbose_name='Город')),
                ('map', models.CharField(blank=True, max_length=250, null=True, verbose_name='местоположение на карте')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
