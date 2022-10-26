from rest_framework import generics
from rest_api.serializers import BookSerializer
from images_app.models import Libary

class LibaryView(generics.ListCreateAPIView,
                 generics.DestroyAPIView,
                 generics.UpdateAPIView):
    queryset = Libary.objects.all()
    serializer_class = BookSerializer
    ordering_fields = ['id']
