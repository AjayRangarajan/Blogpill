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
        field_ids=['blog-name','blog-content','blog-image','blog-image-link','alt-msg','blog-tags']
        field_labels=['Blog Title','Blog Content','Blog Image','Blog Image Link','Alt msg','Tags']
        field_placeholders=['Blog Title','Blog Content',None,'Blog Image link','description of the image',None]

        for i in range(len(self.fields)):
            field=fields_key_list[i]
            self.fields[field].widget.attrs={
                'id':field_ids[i],
                'placeholder':field_placeholders[i],
            }
            self.fields[field].label=field_labels[i]