from django.contrib.auth.models import User
from .models import CAChineseUser
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import random
from django.core.mail import send_mail

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CAChineseUser
        fields = '__all__'


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

        # 1. Create Django User
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # 2. Create profile
        profile = CAChineseUser.objects.create(
            user=user,
            nickname=nickname,
            chinese_name=chinese_name,
            level=level,
            avatar=avatar,
            email=email
        )

        # 🔥 3. AUTO SEND VERIFICATION CODE
        code = str(random.randint(100000, 999999))
        profile.verification_code = code
        profile.save()

        send_mail(
            subject="Email verification",
            message=f"Your verification code is: {code}",
            from_email="no-reply@yourapp.com",
            recipient_list=[email],
        )

        return profile


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        user = authenticate(
            username=data['email'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        profile = CAChineseUser.objects.get(user=user)

        if not profile.is_verified:
            raise serializers.ValidationError("This account has not been verified")

        refresh = RefreshToken.for_user(user)

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user_id': user.id,
            'email': user.email
        }

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()

    def validate(self, attrs):
        email = attrs["email"]
        code = str(attrs["code"])  # make sure string
        user = CAChineseUser.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("User not found.")
        if user.is_verified:
            raise serializers.ValidationError("Email already verified.")
        if user.verification_code != code:
            raise serializers.ValidationError("Invalid verification code.")
        attrs["user"] = user
        return attrs

    def save(self):
        user = self.validated_data["user"]
        user.is_verified = True
        user.verification_code = None
        user.save()
        return user
