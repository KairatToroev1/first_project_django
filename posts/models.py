from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'id': self.id})
