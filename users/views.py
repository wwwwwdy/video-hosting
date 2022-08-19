from rest_framework import generics

from users.models import CustomUser
from users.serializers import UserRegistrationSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = CustomUser.objects.all()
