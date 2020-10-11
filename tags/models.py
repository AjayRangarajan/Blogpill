from django.db import models

class Tags(models.Model):

    name=models.CharField(max_length=50)
    description=models.CharField(max_length=300,blank=True,null=True)
    
    def __str__(self):
        return self.name
