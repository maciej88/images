from rest_framework import generics
from rest_api.serializers import LibraryUpdateSerializer
from images_app.models import Library
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView



class LibraryListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api.html'

    def get(self, request):
        queryset = Library.objects.all()
        return Response({'queryset': queryset})

    # def post(self, request):
    #     queryset = Libary.objects.all()
    #     activation = get_data()
    #     return Response({'queryset': queryset, 'activation':activation})


class LibraryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibraryUpdateSerializer

class LibraryCreateView(generics.CreateAPIView):
    serializer_class = LibraryUpdateSerializer

