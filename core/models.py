from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
import uuid

user = get_user_model()
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    Profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png' ) 
    location = models.CharField(max_length=100, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption =models.TextField()
    timeStamp = models.DateTimeField(default=datetime.now)
    # (auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user
    
    
class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower =models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user
    