from django.db import models
from vocabulary.models import HSKWord
from django.conf import settings


class Flashcard(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="flashcards"
    )

    vocabulary = models.ForeignKey(
        HSKWord,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    word = models.CharField(max_length=50, blank=True, null=True)
    pinyin = models.CharField(max_length=100, blank=True, null=True)
    translation = models.CharField(max_length=200, blank=True, null=True)

    timer = models.PositiveIntegerField(default=5)
    mastered = models.BooleanField(default=False)
    is_user_card = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
