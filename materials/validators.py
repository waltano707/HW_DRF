from rest_framework.serializers import ValidationError

forbidden_video = ["^(https?://)?(www\.)?youtube\.com/?$"]


def validate_forbidden_video(value):
    """Валидатор, проверяющий запрет ссылки на Youtube"""
    if value in forbidden_video:
        raise ValidationError(
            "Невозможно загрузить данное видео, присутствует ссылка на youtube.com"
        )
