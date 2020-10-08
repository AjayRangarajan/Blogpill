from django.db import models
# from cloudinary.models import CloudinaryField

class Authors(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField(blank=False)
    profile_pic=models.ImageField(upload_to="author_profiles",blank=True,null=True)
    # profile_pic=CloudinaryField('image')
    author_image_link=models.URLField(blank=True,null=True)
    alt_msg=models.CharField(max_length=100,default="Author's Profile picture")

    def __str__(self):
        return self.name
