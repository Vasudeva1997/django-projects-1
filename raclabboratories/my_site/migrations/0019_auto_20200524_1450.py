# Generated by Django 3.0.3 on 2020-05-24 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0018_auto_20200524_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 14, 50, 42, 366935)),
        ),
    ]