from rest_framework import generics
from rest_framework import viewsets
from .models import Flashcard
from .serializers import FlashcardSerializer,CreateFlashCard
from rest_framework.permissions import IsAuthenticated

class FlashcardViewSet(viewsets.ModelViewSet):
    serializer_class = FlashcardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Flashcard.objects.filter(user=self.request.user)
        level = self.request.query_params.get('level')
        if level:
            qs = qs.filter(vocabulary__level=level)
        return qs


class CreateFlashcard(generics.CreateAPIView):
    serializer_class = CreateFlashCard
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}
