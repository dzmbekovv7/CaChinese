from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ListeningItem
from .serializers import ListeningItemSerializer, ListeningQuestionSerializer
from .serializers import ListeningUserAnswerSerializer

class getListeningItem(generics.ListAPIView):
    serializer_class = ListeningItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_lvl = user.profile.level

        return ListeningItem.objects.filter(hsk_level=user_lvl)

class getListeningQuestion(generics.ListAPIView):
    serializer_class = ListeningQuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        listening_id = self.kwargs['listening_id']

        return ListeningItem.objects.filter(listening_id=listening_id)

class getUserAnswer(generics.CreateAPIView):
    serializer_class = ListeningUserAnswerSerializer
    permission_classes = [IsAuthenticated]