from django.db import models
from vocabulary.models import HSKWord


class Flashcard(models.Model):
    # If this is a system card (HSK), link to existing vocabulary
    vocabulary = models.ForeignKey(HSKWord, on_delete=models.CASCADE, null=True, blank=True)

    # For user-created cards not in HSK
    word = models.CharField(max_length=50, blank=True, null=True)
    pinyin = models.CharField(max_length=100, blank=True, null=True)
    translation = models.CharField(max_length=200, blank=True, null=True)

    timer = models.PositiveIntegerField(default=5)
    mastered = models.BooleanField(default=False)
    is_user_card = models.BooleanField(default=False)  # distinguish system vs user cards
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.vocabulary:
            return f"HSK: {self.vocabulary.hanzi}"
        return self.word or "Unknown Card"
