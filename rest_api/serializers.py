from images_app.models import Libary
from rest_framework import serializers


class LibaryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libary
        fields = ('id', 'album_id', 'title', 'link', 'width', 'height')

class LibaryUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libary
        fields = ('id', 'album_id', 'title', 'link')