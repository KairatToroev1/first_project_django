from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'body', ]

admin.site.register(Post, PostAdmin)
