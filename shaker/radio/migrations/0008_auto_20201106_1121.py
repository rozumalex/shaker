# Generated by Django 3.1.2 on 2020-11-06 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0007_auto_20201106_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='background',
            old_name='file',
            new_name='image',
        ),
    ]