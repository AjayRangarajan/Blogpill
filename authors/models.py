from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    profile_pic=CloudinaryField('image')
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True,null=True)
    # profile_pic = models.ImageField(upload_to='profile_pics',default='profile_pics/default_profile_pic.png',blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} - Profile'
