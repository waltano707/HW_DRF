from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    course = SerializerMethodField()

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer()
    count_lesson = SerializerMethodField()

    def get_count_lesson(self, obj):
        return obj.courses.count()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = ("id", "title", "description", "lessons", "count_lesson")


class CourseDetailSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    lesson = LessonSerializer()

    def get_count_lesson(self, obj):
        return obj.courses.count()

    class Meta:
        model = Course
        fields = "__all__"
