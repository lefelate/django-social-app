from django.contrib import admin
from .models import FollowersCount, Profile, Post, LikePost

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','timeStamp']
    list_filter = []
    search_fields = ['id _user', 'user']
    
admin.site.register(Profile, ProfileAdmin)
    
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','caption','timeStamp']
    list_filter = ['user','caption']
    search_fields = ['id _user', 'user']
    
admin.site.register(Post, PostAdmin)

admin.site.register(LikePost)
admin.site.register(FollowersCount)

    