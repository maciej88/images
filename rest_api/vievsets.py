from rest_framework import generics
from rest_api.serializers import LibaryUpdateSerializer
from images_app.models import Libary
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView



class LibaryListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api.html'

    def get(self, request):
        queryset = Libary.objects.all()
        return Response({'queryset': queryset})

    # def post(self, request):
    #     queryset = Libary.objects.all()
    #     activation = get_data()
    #     return Response({'queryset': queryset, 'activation':activation})


class LibaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libary.objects.all()
    serializer_class = LibaryUpdateSerializer

class LibaryCreateView(generics.CreateAPIView):
    serializer_class = LibaryUpdateSerializer

