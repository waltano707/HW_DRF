from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payment, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone", "city", "avatar")


class PaymentSerializer(ModelSerializer):
    course_name = SerializerMethodField()

    def get_course_name(self, obj):
        return obj.courses.name

    class Meta:
        model = Payment
        fields = "__all__"
