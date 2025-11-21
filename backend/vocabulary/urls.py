from django.urls import path
from .views import HSKWordListView

urlpatterns = [
    path('', HSKWordListView.as_view(), name='hsk-list'),
]
