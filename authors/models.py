from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
class Authors(models.Model):
    default=models.OneToOneField(User,on_delete=models.CASCADE,related_name='author')
    # profile_pic=models.ImageField(upload_to="author_profiles",blank=True,null=True)
    profile_pic=CloudinaryField('image')
    profile_image_link=models.URLField(blank=True,null=True)
    alt_msg=models.CharField(max_length=100,default="Author's Profile picture")

    def __str__(self):
        return self.default.username