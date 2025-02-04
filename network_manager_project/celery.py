import os
from celery import Celery

# Установите переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network_manager_project.settings')

# Создайте экземпляр Celery
app = Celery('network_manager_project')

# Загрузите настройки из файла settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находите и регистрируйте задачи в приложениях Django
app.autodiscover_tasks()
