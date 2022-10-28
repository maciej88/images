from django.urls import reverse

from django.db import models



# Create your models here.
class Libary(models.Model):
    id = models.IntegerField(null=False, blank=True, primary_key=True)
    album_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=300)
    link = models.ImageField(null=True, blank=True, upload_to='images/', height_field="height", width_field="width")
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)

    def __str__(self):
        return self.link


    # with open(link, 'rb') as f:
    #     content = f.read()
    # hex = binascii.hexlify(content)
    # def get_dominant_color(self, link):
    #     img = link.copy()
    #     img = img.convert("HEX")
    #     img = img.resize((1,1), resample=0)
    #     dominant_color = img.getpixel((0,0))
    #     return dominant_color
    #
    # dominant_color = models.IntegerField(null=True)