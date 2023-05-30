# Generated by Django 4.2.1 on 2023-05-30 15:56

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
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.PositiveIntegerField(verbose_name='сколько рядов')),
                ('columns', models.PositiveIntegerField(verbose_name='сколько столбцов')),
                ('prizes', models.TextField(max_length=100, verbose_name='призы')),
            ],
            options={
                'verbose_name': 'ячейка',
                'verbose_name_plural': 'ячейки',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.PositiveIntegerField(verbose_name='ряд')),
                ('column', models.PositiveIntegerField(verbose_name='столбец')),
                ('prize_item', models.CharField(max_length=100, verbose_name='приз')),
                ('box', models.ManyToManyField(to='draw.box', verbose_name='ячейка')),
            ],
            options={
                'verbose_name': 'Приз',
                'verbose_name_plural': 'Призы',
            },
        ),
        migrations.CreateModel(
            name='MoreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название розыгрыша')),
                ('how_prize_true', models.TextField(max_length=100, verbose_name='В данном розыгрыше присутствуют такие призы как: ')),
                ('how_prize_win', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.prize')),
                ('winners', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Победители')),
            ],
            options={
                'verbose_name': 'Последняя аренда',
                'verbose_name_plural': 'последние аренды',
            },
        ),
    ]
