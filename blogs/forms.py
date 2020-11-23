from django.forms import ModelForm
from blogs.models import Blogs

class BlogCreationForm(ModelForm):
    class Meta:
        model=Blogs
        fields= '__all__'
        exclude=['published_date','author']

    def __init__(self,*args,**kwargs):
        super(BlogCreationForm,self).__init__(*args,**kwargs)
        fields_key_list=list(self.fields.keys())
        field_ids=['blog-title','blog-content','blog-image','blog-image-link','alt-msg','blog-tags']
        field_labels=['Blog Title','Blog Content','Blog Image','Blog Image Link','Alt msg','Add Tags']
        field_placeholders=['Add a Title for the Blog','Blog Content (Add HTML tags for markup)','Add Image','Blog Image link','description for the image',None]

        for i in range(len(self.fields)):
            field=fields_key_list[i]

            self.fields[field].widget.attrs={
                'id':field_ids[i],
                'placeholder':field_placeholders[i],
            }
            self.fields[field].label=field_labels[i]

class BlogUpdateForm(ModelForm):
    class Meta:
        model=Blogs
        fields= '__all__'
        exclude=['published_date','author']

    def __init__(self,*args,**kwargs):
        super(BlogUpdateForm,self).__init__(*args,**kwargs)
        fields_key_list=list(self.fields.keys())
        field_ids=['blog-title','blog-content','blog-image','blog-image-link','alt-msg','blog-tags']
        field_labels=['Blog Title','Blog Content','Blog Image','Blog Image Link','Alt msg','Add Tags']
        field_placeholders=['Add a Title for the Blog','Blog Content (Add HTML tags for markup)','Add Image','Blog Image link','description for the image',None]

        for i in range(len(self.fields)):
            field=fields_key_list[i]

            self.fields[field].widget.attrs={
                'id':field_ids[i],
                'placeholder':field_placeholders[i],
            }
            self.fields[field].label=field_labels[i]