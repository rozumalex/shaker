from django.db import models


class Song(models.Model):
    file = models.FileField(upload_to='music/uploads/')

    def __str__(self):
        return str(self.file)
