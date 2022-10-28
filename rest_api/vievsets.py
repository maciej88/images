from rest_framework import generics
from rest_api.serializers import LibaryListSerializer, LibaryUpdateSerializer
from images_app.models import Libary

class LibaryListView(generics.ListAPIView):
    queryset = Libary.objects.all()
    serializer_class = LibaryListSerializer
    ordering_fields = ['id']


class LibaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libary.objects.all()
    serializer_class = LibaryUpdateSerializer

class LibaryCreateView(generics.CreateAPIView):
    serializer_class = LibaryUpdateSerializer