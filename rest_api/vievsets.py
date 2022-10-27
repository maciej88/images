from rest_framework import generics
from rest_api.serializers import BookSerializer
from images_app.models import Libary

class LibaryView(generics.ListCreateAPIView):
    queryset = Libary.objects.all()
    serializer_class = BookSerializer
    ordering_fields = ['id']


class LibaryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libary.objects.all()
    serializer_class = BookSerializer
