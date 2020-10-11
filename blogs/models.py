from django.db import models
from django.utils import timezone
import datetime
# from cloudinary.models import CloudinaryField

class Blogs(models.Model):

    name=models.CharField(max_length=100)
    title=models.CharField(max_length=300)
    content=models.TextField(max_length=5000)
    published_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey("authors.Authors",on_delete=models.CASCADE,related_name="blogs")
    image=models.ImageField(upload_to="blog_images",blank=True,null=True)
    # image=CloudinaryField('image')
    image_link=models.URLField(blank=True,null=True)
    alt_msg=models.CharField(default="Image related to this blog",max_length=200)
    tags=models.ManyToManyField("tags.Tags",related_name="blogs")


    def was_published_recently(self):
        return self.published_date >= timezone.now()-datetime.timedelta(days=60)
        
    def __str__(self):
        return self.title