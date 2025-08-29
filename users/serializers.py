from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payment, Subscription, User


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


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
