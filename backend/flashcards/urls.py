from django.urls import path
from .views import FlashcardViewSet

flashcard_list = FlashcardViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

flashcard_detail = FlashcardViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', flashcard_list, name='flashcard-list'),
    path('<int:pk>/', flashcard_detail, name='flashcard-detail'),
]
