# Generated by Django 3.1.1 on 2020-10-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_content',
            field=models.TextField(max_length=5000),
        ),
    ]
