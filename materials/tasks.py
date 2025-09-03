from celery import shared_task
from django.core.mail import send_mail
from datetime import timedelta
from django.utils.timezone import now

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_message_about_update_course(email):
    """Отправка сообщения студенту о том, что курс обновлен"""
    send_mail("Обновление", "Курс обновлен", EMAIL_HOST_USER, [email])


@shared_task
def inactive_users():
    """Проверка студентов по дате последнего входа, происходит деакцивация студента,
    который не заходил в систему более 30 дней."""
    cutoff_date = now() - timedelta(days=30)
    users_to_block = User.objects.filter(last_login__lt=cutoff_date, is_active=True)
    for user in users_to_block:
        user.is_active = False
        user.save()
