# Generated by Django 4.2.1 on 2023-06-06 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
        ('account', '0005_remove_user_history_user_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_history', to='main_page.rentcar', verbose_name='История аренды'),
        ),
    ]
