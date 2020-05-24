# Generated by Django 3.0.3 on 2020-05-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0005_postdetails_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postdetails',
            old_name='sub_cateogry',
            new_name='solubility',
        ),
        migrations.AddField(
            model_name='postdetails',
            name='mol_fm',
            field=models.CharField(default=None, max_length=333),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postdetails',
            name='mol_wt',
            field=models.CharField(default=None, max_length=333),
            preserve_default=False,
        ),
    ]