from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        blank=True,
        verbose_name="Картинка",
        help_text="Загрузите превью (картинка)",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        blank=True,
        verbose_name="Картинка",
        help_text="Загрузите превью (картинка)",
    )
    link = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Курс",
        help_text="Выберите курс",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
