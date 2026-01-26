from rest_framework import generics
from rest_framework import viewsets
from .models import Flashcard
from .serializers import FlashcardSerializer,CreateFlashCardSerializer, ChangeFlashcardSerializer
from rest_framework.permissions import IsAuthenticated

class getFlashcards(generics.ListAPIView):
    serializer_class = FlashcardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Flashcard.objects.filter(user=self.request.user)

class postFlashcard(generics.CreateAPIView):
    serializer_class = CreateFlashCardSerializer
    permission_classes = [IsAuthenticated]

class changeFlashcard(generics.UpdateAPIView):
    serializer_class = ChangeFlashcardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Flashcard.objects.filter(user=self.request.user)

class deleteFlashCard(generics.DestroyAPIView):
    serializer_class = FlashcardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Flashcard.objects.filter(user=self.request.user)