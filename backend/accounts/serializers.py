from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CAChineseUser

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    nickname = serializers.CharField()
    level = serializers.IntegerField()
    chinese_name = serializers.CharField(required=False, allow_blank=True)
    avatar = serializers.ImageField(required=False)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        nickname = validated_data['nickname']
        level = validated_data['level']
        chinese_name = validated_data.get('chinese_name', "")
        avatar = validated_data.get('avatar', None)

        # 1. Create Django User (username = email)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # 2. Create CAChineseUser profile
        profile = CAChineseUser.objects.create(
            user=user,
            nickname=nickname,
            chinese_name=chinese_name,
            level=level,
            avatar=avatar
        )

        return profile
