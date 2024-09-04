from rest_framework.serializers import Serializer, ModelSerializer

from UserApp.models import Foydalanuvchilar


class RegistrationSeralizer(ModelSerializer):
    class Meta:
        model = Foydalanuvchilar
        fields = ("name", 'surname', "email", 'username')


class LoginSeralizer(ModelSerializer):
    class Meta:
        model = Foydalanuvchilar
        fields = ("email",)
