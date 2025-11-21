from rest_framework import generics
from .models import HSKWord
from .serializers import HSKWordSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class HSKWordListView(generics.ListAPIView):
    queryset = HSKWord.objects.all().order_by('id')
    serializer_class = HSKWordSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['level']
    search_fields = ['hanzi', 'pinyin', 'translation']
