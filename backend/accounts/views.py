from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import CAChineseUser
from .serializers import RegisterSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class AllUsers(generics.ListAPIView):
    queryset = CAChineseUser.objects.all().order_by('id')
    serializer_class = RegisterSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

class AllUserDetail(generics.RetrieveAPIView):
    queryset = CAChineseUser.objects.all()
    serializer_class = RegisterSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = CAChineseUser.objects.all()