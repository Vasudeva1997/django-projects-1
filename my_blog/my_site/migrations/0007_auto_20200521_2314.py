# Generated by Django 3.0.3 on 2020-05-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0006_auto_20200521_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='post',
            name='image_file',
            field=models.ImageField(upload_to='post_pics'),
        ),
    ]
