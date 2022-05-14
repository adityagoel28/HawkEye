from django.db import models

# Create your models here.

class videoUploader(models.Model):
    video = models.FileField(upload_to='video/')
    url = models.CharField(max_length=255)