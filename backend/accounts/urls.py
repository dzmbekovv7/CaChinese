from django.urls import path
from .views import AllUsers, AllUserDetail, RegisterUser, LoginUser, VerifyEmail

urlpatterns = [
    path('all-users', AllUsers.as_view(), name='allUsers'),
    path('detail-user/<int:pk>',AllUserDetail.as_view(), name='detailUser'),
    path('verify-email', VerifyEmail.as_view(), name='verifyEmail'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
]