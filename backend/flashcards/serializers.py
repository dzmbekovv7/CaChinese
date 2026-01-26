from rest_framework import serializers
from .models import Flashcard



class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'

class CreateFlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['word', 'pinyin', 'translation']

    def create(self, validated_data):
        user = self.context['request'].user
        return Flashcard.objects.create(
            user=user,
            is_user_card = True,
            **validated_data
        )

class ChangeFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['word', 'pinyin', 'translation']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

