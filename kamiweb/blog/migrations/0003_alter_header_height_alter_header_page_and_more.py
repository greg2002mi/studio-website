# Generated by Django 5.0.7 on 2024-08-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='header',
            name='page',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Home'), (2, 'Video case'), (3, 'Reel'), (4, 'Photography'), (5, 'Grachic Design'), (6, 'Website'), (7, 'SMM'), (8, 'Services'), (9, 'About Studio'), (10, 'Clients'), (11, 'Reviews'), (12, 'Contacts'), (13, 'Make an order'), (14, 'Call me')], default=0),
        ),
        migrations.AlterField(
            model_name='header',
            name='top',
            field=models.IntegerField(default=0),
        ),
    ]
