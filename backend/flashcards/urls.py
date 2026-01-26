from django.urls import path

from .views import getFlashcards, postFlashcard, changeFlashcard, deleteFlashCard

urlpatterns = [
    path('flashcards', getFlashcards.as_view(), name='flashcards'),
    path('postFlashcard', postFlashcard.as_view(), name='postFlashcard'),
    path('flashcards/<int:pk>', changeFlashcard.as_view(), name='flashcards'),
    path('flashcards/<int:pk>/delete', deleteFlashCard.as_view(), name='flashcards'),

]
