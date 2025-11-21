from django.db import models

class HSKWord(models.Model):
    LEVEL_CHOICES = [
        (1, 'HSK 1'),
        (2, 'HSK 2'),
        (3, 'HSK 3'),
        (4, 'HSK 4'),
        (5, 'HSK 5'),
        (6, 'HSK 6'),
    ]

    hanzi = models.CharField(max_length=50)          # 中文
    pinyin = models.CharField(max_length=100)        # pinyin
    translation = models.CharField(max_length=200)   # meaning in English
    level = models.IntegerField(choices=LEVEL_CHOICES)
    example_cn = models.CharField(max_length=255, blank=True, null=True)
    example_en = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.hanzi} ({self.pinyin}) – HSK {self.level}"
