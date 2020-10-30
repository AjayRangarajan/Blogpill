from django.forms import ModelForm
from blogs.models import Blogs

class BlogCreationForm(ModelForm):
    class Meta:
        model=Blogs
        fields= '__all__'
        exclude=['published_date','author']