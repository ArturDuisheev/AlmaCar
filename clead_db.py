import os
import django

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Импортируем модели
from draw.models import Box

# Очищаем таблицу
Box.objects.all().delete()
