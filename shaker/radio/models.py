from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Track(models.Model):
    file = models.FileField(upload_to='music/uploads/')
    date_uploaded = models.DateTimeField(default=timezone.now)
    user_uploaded = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_uploaded')
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.IntegerField()
    track_number = models.IntegerField()

    def __str__(self):
        return str(self.file)
