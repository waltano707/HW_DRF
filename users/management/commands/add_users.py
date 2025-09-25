from django.core.management.base import BaseCommand

from materials.models import Course
from users.models import Payment, User


class Command(BaseCommand):
    help = "Add test payment to the database"

    def handle(self, *args, **kwargs):
        user, _ = User.objects.get_or_create(email="test@example.com")

        course = Course.objects.first()

        if not course:
            raise Exception("Нет курсов в базе данных")

        payments = [
            {"user": user, "payment_amount": 100, "payment_method": "Наличные"},
            {"user": user, "payment_amount": 300, "payment_method": "Перевод на счет"},
            {
                "user": user,
                "paid_course": course,
                "payment_amount": 100,
                "payment_method": "Наличные",
            },
        ]

        for payment_data in payments:
            payment, created = Payment.objects.get_or_create(**payment_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added payment: {user.email}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Payment already exists: {user.email}")
                )
