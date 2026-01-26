from .models import Grammar, GrammarQuestion, UserAnswer, UserGrammarProgress
from rest_framework import serializers

class GrammarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grammar
        fields = '__all__'

class GrammarQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarQuestion
        fields = '__all__'

class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['grammar', 'selected_answers']

    def create(self, validated_data):
        user = self.context['request'].user
        grammar = validated_data['grammar']
        selected_answers = validated_data['selected_answers']

        questions = list(grammar.questions.all().order_by('id'))
        score = 0
        for i, question in enumerate(questions):
            if i < len(selected_answers):
                if str(selected_answers[i]).strip() == question.correct_answer.strip():
                    score += 1
        completed = ( score == len(questions) )

        user_answer = UserAnswer.objects.create(
            user = user,
            grammar = grammar,
            selected_answers = selected_answers,
            completed = completed,
            score = score,

        )

        progress, _ = UserGrammarProgress.objects.get_or_create(
                    user=user,
                    grammar=grammar,
                    defaults={'score': 0, 'completed': False}
                )

        progress.score = score
        progress.completed = completed
        progress.save()

        return user_answer
