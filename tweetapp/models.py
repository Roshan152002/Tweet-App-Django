from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet_msg = models.CharField(max_length=255)
    photo = models.FileField(upload_to='tweet_photos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'tweet by {self.user.username}'