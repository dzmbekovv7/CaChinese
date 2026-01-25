from django.urls import path
from .views import getListeningItem
urlpatterns = [
    path('listening-item', getListeningItem.as_view(), name='listening-item'),
]