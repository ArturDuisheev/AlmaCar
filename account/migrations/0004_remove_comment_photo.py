# Generated by Django 4.2.1 on 2023-06-01 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_delete_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
    ]
