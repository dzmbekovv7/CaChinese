from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CAChineseUser
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer, VerifyEmailSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class AllUsers(generics.ListAPIView):
    queryset = CAChineseUser.objects.all().order_by('id')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

class AllUserDetail(generics.RetrieveAPIView):
    queryset = CAChineseUser.objects.all()
    serializer_class = UserSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = CAChineseUser.objects.all()

class VerifyEmail(generics.CreateAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = [AllowAny]

class LoginUser(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
