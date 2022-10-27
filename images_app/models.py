from django.db import models


# Create your models here.
class Libary(models.Model):
    synthetic_id = models.IntegerField(null=True, blank=True)
    album_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=300)
    link = models.ImageField(null=True, blank=True, upload_to='images/')