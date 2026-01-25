from rest_framework import generics
from .models import ListeningItem
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import ListeningItemSerializer

class getListeningItem(generics.ListAPIView):
    queryset = ListeningItem.objects.all()
    serializer_class = ListeningItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
