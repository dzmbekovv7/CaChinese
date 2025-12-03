from django.urls import path
from .views import AllUsers, AllUserDetail, RegisterUser

urlpatterns = [
    path('all-users', AllUsers.as_view(), name='allUsers'),
    path('detail-user/<int:pk>',AllUserDetail.as_view(), name='detailUser'),
    path('register', RegisterUser.as_view(), name='register'),
]
