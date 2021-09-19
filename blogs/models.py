from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime

class Blogs(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    image=CloudinaryField('image')
    # image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,related_name='blog', on_delete=models.CASCADE, blank=True, null=True)

    def was_published_recently(self):
        return self.published_date >= timezone.now()-datetime.timedelta(days=60)

    def __str__(self):
        return self.title