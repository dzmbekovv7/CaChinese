from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import HSKWord
from .serializers import HSKWordSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class HSKWordListView(generics.ListAPIView):
    serializer_class = HSKWordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['level']
    search_fields = ['hanzi', 'pinyin', 'translation']
    def get_queryset(self):
        user = self.request.user
        user_lvl = user.profile.level

        return HSKWord.objects.filter(level=user_lvl)

class HSKWordFullListView(generics.ListAPIView):
    queryset = HSKWord.objects.all()
    serializer_class = HSKWordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]