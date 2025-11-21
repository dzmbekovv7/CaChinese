from rest_framework import serializers
from .models import HSKWord

class HSKWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSKWord
        fields = '__all__'
