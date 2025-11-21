from django.contrib import admin
from .models import HSKWord

@admin.register(HSKWord)
class HSKWordAdmin(admin.ModelAdmin):
    list_display = ('hanzi', 'pinyin', 'translation', 'level')
    list_filter = ('level',)
    search_fields = ('hanzi', 'pinyin', 'translation')
