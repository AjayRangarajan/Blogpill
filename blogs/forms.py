from django import forms
# from django.forms import fields 
from .models import Blogs

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        exclude = ['published_date','author',]

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        exclude = ['published_date','author',]