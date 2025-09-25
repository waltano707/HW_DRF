from rest_framework.serializers import (ModelSerializer, SerializerMethodField,
                                        URLField)

from materials.models import Course, Lesson
from materials.validators import validate_forbidden_video


class LessonSerializer(ModelSerializer):
    """Сериализация урока"""

    link = URLField(validators=[validate_forbidden_video], required=False)

    class Meta:
        model = Lesson
        fields = ["id", "title", "description", "link", "course", "owner"]


class CourseSerializer(ModelSerializer):
    """Сериализация курса с количеством уроков"""

    lesson = LessonSerializer()
    count_lesson = SerializerMethodField()

    def get_count_lesson(self, obj):
        return obj.courses.count()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = ("id", "title", "description", "lesson", "count_lesson")


class CourseDetailSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    lesson = LessonSerializer()

    def get_count_lesson(self, obj):
        return obj.courses.count()

    class Meta:
        model = Course
        fields = "__all__"
