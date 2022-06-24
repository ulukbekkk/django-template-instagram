from django.db import models


class Post(models.Model):
    user = models.ForeignKey('account.User', related_name='post', on_delete=models.CASCADE)
    body = models.TextField()
    location = models.CharField(max_length=40, blank=True)
    images = models.ImageField(upload_to='images', blank=True)
    videos = models.FileField(upload_to='videos', blank=True)
    created_at = models.DateField(auto_now_add=True)



