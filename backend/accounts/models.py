from django.db import models
from django.contrib.auth.models import User

class CAChineseUser(models.Model):
    LEVELS_OF_USER = [
        (1, 'HSK1'),
        (2, 'HSK2'),
        (3, 'HSK3'),
        (4, 'HSK4'),
        (5, 'HSK5'),
        (6, 'HSK6'),
    ]
    BACKGROUND_COLOR = [
        (1, 'light'),
        (2, 'dark')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, blank=True)
    chinese_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    level = models.IntegerField(choices=LEVELS_OF_USER, default=1)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    daily_xp = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    daily_goal = models.IntegerField(default=20)
    joined_at = models.DateTimeField(auto_now_add=True)

    theme = models.IntegerField(choices=BACKGROUND_COLOR, default=1)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=50, blank=True, null=True)
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname or self.user.username
