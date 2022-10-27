from images_app.models import Libary
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libary
        fields = ('id', 'album_id', 'title', 'link')