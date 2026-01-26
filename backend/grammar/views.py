from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Grammar, GrammarQuestion
from .serializers import GrammarSerializer, GrammarQuestionSerializer, UserAnswerSerializer

class getGrammarView(generics.ListAPIView):
    serializer_class = GrammarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_level = user.profile.level

        return Grammar.objects.filter(hsk_level=user_level)

class getGrammarQuestion(generics.ListAPIView):
    serializer_class = GrammarQuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        grammar_id = self.kwargs['grammar_id']
        return GrammarQuestion.objects.filter(grammar_id=grammar_id)

class userAnswerView(generics.CreateAPIView):
    serializer_class = UserAnswerSerializer
    permission_classes = [IsAuthenticated]
