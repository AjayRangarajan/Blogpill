# Generated by Django 3.1.1 on 2020-10-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20201003_0634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_image_link',
            new_name='image_link',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_title',
            new_name='title',
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('blog', models.ManyToManyField(to='blogs.Blogs')),
            ],
        ),
    ]
