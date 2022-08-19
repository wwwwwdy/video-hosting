from djoser.serializers import UserCreateSerializer
from rest_framework import serializers


class UserRegistrationSerializer(UserCreateSerializer):
    email = serializers.EmailField(max_length=254,
                                   help_text='Введите почту')
    username = serializers.CharField(max_length=150,
                                     help_text='Введите имя пользователя')
    first_name = serializers.CharField(max_length=150,
                                       help_text='Введите ваше имя')
    last_name = serializers.CharField(max_length=150,
                                      help_text='Введите вашу фамилию')

    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'id', 'username',
                  'first_name', 'last_name', 'password')
