from .models import ListeningItem
from rest_framework import serializers

class ListeningItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = ListeningItem
        field = '___all___'