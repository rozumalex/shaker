# Generated by Django 3.0.8 on 2020-07-15 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('radio', '0001_squashed_0009_auto_20200715_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='track_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='track',
            name='user_uploaded',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user_uploaded',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
