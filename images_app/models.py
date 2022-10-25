from django.db import models


# Create your models here.
class Libary(models.Model):
    album_id = models.IntegerField(max_length=200)
    title = models.CharField(max_length=300)
    link = models.ImageField(upload_to='images/')
