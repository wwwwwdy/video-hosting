from django.db import models

from users.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название категории')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название тэга')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название видеозаписи')
    description = models.TextField(max_length=400, verbose_name='Описание')
    upload_date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='media/')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='videos')
    categories = models.ManyToManyField(Category, related_name='videos', verbose_name='Категории')
    tags = models.ManyToManyField(Tag, related_name='videos', verbose_name='Тэги')

    class Meta:
        verbose_name = 'Видеозапись'
        verbose_name_plural = 'Видеозаписи'
        ordering = ('-upload_date',)

    def __str__(self):
        return self.title
