# Generated by Django 3.0.3 on 2020-05-24 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0014_auto_20200524_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='post',
        ),
    ]