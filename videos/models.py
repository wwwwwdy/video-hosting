from django.db import models

from users.models import CustomUser


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название видеозаписи')
    description = models.TextField(max_length=400, verbose_name='Описание')
    upload_date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='media/')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='videos')
