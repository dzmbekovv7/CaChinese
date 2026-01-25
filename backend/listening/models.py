from django.db import models
from django.contrib.auth.models import User

class ListeningItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='listening_audios/')  # or video_file
    transcript = models.TextField(blank=True)
    hsk_level = models.IntegerField(choices=[(i,i) for i in range(1,7)])
    created_at = models.DateTimeField(auto_now_add=True)

class ListeningQuestion(models.Model):
    listening_item = models.ForeignKey(ListeningItem, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[('mcq','Multiple Choice'), ('tf','True/False'), ('fill','Fill in the blank')])
    options = models.JSONField(blank=True, null=True)  # for MCQs
    correct_answer = models.TextField()

class UserListeningProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listening_item = models.ForeignKey(ListeningItem, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed = models.BooleanField(default=False)
    last_attempted = models.DateTimeField(auto_now=True)
