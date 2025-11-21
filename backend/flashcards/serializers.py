from rest_framework import serializers
from .models import Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
    word = serializers.SerializerMethodField()
    pinyin = serializers.SerializerMethodField()
    translation = serializers.SerializerMethodField()

    class Meta:
        model = Flashcard
        fields = ['id','word','pinyin','translation','level','timer','mastered','is_user_card']

    def get_level(self, obj):
        if obj.vocabulary:
            return obj.vocabulary.level
        return None

    def get_word(self, obj):
        if obj.is_user_card:
            return obj.word
        if obj.vocabulary:
            return obj.vocabulary.hanzi
        return None

    def get_pinyin(self, obj):
        if obj.is_user_card:
            return obj.pinyin
        if obj.vocabulary:
            return obj.vocabulary.pinyin
        return None

    def get_translation(self, obj):
        if obj.is_user_card:
            return obj.translation
        if obj.vocabulary:
            return obj.vocabulary.translation
        return None
