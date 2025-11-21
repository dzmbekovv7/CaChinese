from rest_framework import viewsets
from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardViewSet(viewsets.ModelViewSet):
    serializer_class = FlashcardSerializer
    permission_classes = []

    def get_queryset(self):
        qs = Flashcard.objects.all()
        level = self.request.query_params.get('level')
        if level:
            qs = qs.filter(vocabulary__level=level)
        return qs
