from django.contrib import admin

from videos.models import Video, Category, Tag

admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(Category)
