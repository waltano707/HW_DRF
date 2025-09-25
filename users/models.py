from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    """Модель Пользователь"""

    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите email"
    )
    phone = models.CharField(
        max_length=35, blank=True, verbose_name="Телефон", help_text="Укажите телефон"
    )
    city = models.CharField(
        max_length=35, blank=True, verbose_name="Город", help_text="Укажите город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        verbose_name="Аватар",
        help_text="Загрузите фото",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """Модель Платежи"""

    CASH = "Наличные"
    BANK_TRANSFER = "Перевод на счет"
    PAYMENT_METHOD = (
        (CASH, "Наличные"),
        (BANK_TRANSFER, "Перевод на счет"),
    )

    session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="id сессии",
        help_text="Укажите id сессии",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
    )
    date_payment = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата оплаты",
        help_text="Укажите дату оплаты",
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Оплаченный курс",
        help_text="Укажите оплаченный курс",
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Оплаченный урок",
        help_text="Укажите оплаченный урок",
    )
    payment_amount = models.PositiveIntegerField(
        verbose_name="Сумма оплаты", help_text="Укажите сумму оплаты"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD,
        default=CASH,
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
    )

    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату)",
    )

    def __str__(self):
        return f"{self.paid_course if self.paid_course else self.paid_lesson} - {self.payment_amount}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = (
            "date_payment",
            "payment_method",
        )


class Subscription(models.Model):
    """Модель Подписка"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
        help_text="Укажите пользователя",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        null=True,
        blank=True,
        help_text="Укажите курс",
    )

    def __str__(self):
        return f"{self.user, self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
