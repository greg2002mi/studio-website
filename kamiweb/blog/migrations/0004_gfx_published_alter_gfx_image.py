# Generated by Django 5.0.7 on 2024-08-08 11:34

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_header_height_alter_header_page_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gfx',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gfx',
            name='image',
            field=models.ImageField(upload_to=blog.models.generate_gfxfilename),
        ),
    ]
