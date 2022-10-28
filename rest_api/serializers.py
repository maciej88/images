from images_app.models import Library
from rest_framework import serializers


# class LibraryListSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Library
#         fields = ('id', 'album_id', 'title', 'link', 'width', 'height')

class LibraryUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'album_id', 'title', 'link')