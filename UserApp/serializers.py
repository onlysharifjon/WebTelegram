from rest_framework.serializers import Serializer, ModelSerializer

from UserApp.models import Foydalanuvchilar,ChatModel


class RegistrationSeralizer(ModelSerializer):
    class Meta:
        model = Foydalanuvchilar
        fields = ("name", 'surname', "email", 'username')


class LoginSeralizer(ModelSerializer):
    class Meta:
        model = Foydalanuvchilar
        fields = ("email",)


class ChatSerializer(ModelSerializer):
    class Meta:
        model = ChatModel
        fields = "__all__"