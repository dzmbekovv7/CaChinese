from django.db import models
from django.contrib.auth.models import User

class Grammar(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    example = models.TextField()
    hsk_level = models.IntegerField(choices=[(i, i) for i in range(1, 7)])

    def __str__(self):
        return self.title

class GrammarQuestion(models.Model):
    grammar = models.ForeignKey(
        Grammar,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    question_text = models.TextField()
    question_type = models.CharField(
        max_length=50,
        choices=[
            ('mcq', 'Multiple Choice'),
            ('tf', 'True/False'),
            ('fill', 'Fill in the blank')
        ]
    )
    options = models.JSONField(blank=True, null=True)
    correct_answer = models.TextField()

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grammar = models.ForeignKey(Grammar, on_delete=models.CASCADE)
    selected_answers = models.JSONField()  # list of answers
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    answered_at = models.DateTimeField(auto_now_add=True)


class UserGrammarProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grammar = models.ForeignKey(Grammar, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed = models.BooleanField(default=False)
    last_attempted = models.DateTimeField(auto_now=True)