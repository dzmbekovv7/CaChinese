from django.urls import path
from .views import getGrammarView, getGrammarQuestion, userAnswerView

urlpatterns = [
    path('grammar-items', getGrammarView.as_view(), name='listening-item'),
    path('grammar-items/<int:grammar_id>/questions', getGrammarQuestion.as_view(), name='grammar-questions'),
    path('submit-answer', userAnswerView.as_view(), name='submit-answer'),

]