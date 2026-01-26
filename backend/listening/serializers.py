from .models import ListeningItem, ListeningQuestion, UserListeningAnswer, UserListeningProgress
from rest_framework import serializers

class ListeningItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = ListeningItem
        field = '___all___'

class ListeningQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestion
        field = '___all___'

class ListeningUserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserListeningAnswer
        field = ['listening_item', 'selected_answers']

    def create(self, validated_data):
        user = self.context['request'].user
        listening_item = validated_data['listening_item']
        selected_answers = validated_data['selected_answers']

        questions = list(listening_item.questions.all().orber_by('id'))
        score = 0

        for i, question in enumerate(questions):
            if i < len(selected_answers):
                if str(selected_answers[i]).strip() == question.correct_answer.strip():
                    score += 1
        completed = (score == len(questions))

        user_answer = UserListeningAnswer.objects.create(
            user=user,
            listening_item=listening_item,
            selected_answers=selected_answers,
            score=score,
            completed=completed,
        )

        progress, _ = UserListeningProgress.objects.get_or_create(
            user=user,
            listening_item=listening_item,
            defaults={score: 0, completed: False},
        )

        progress.score = score
        progress.completed = completed
        progress.save()

        return user_answer
