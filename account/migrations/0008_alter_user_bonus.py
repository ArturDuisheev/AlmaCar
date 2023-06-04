# Generated by Django 4.2.1 on 2023-06-04 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0012_alter_detailcar_bonus'),
        ('account', '0007_alter_user_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bonus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_page.detailcar', to_field='bonus'),
        ),
    ]
