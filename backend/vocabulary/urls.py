from django.urls import path
from .views import HSKWordListView, HSKWordFullListView

urlpatterns = [
    path('vocabulary_by_level', HSKWordListView.as_view(), name='hsk-list'),
    path('full_vocabulary', HSKWordFullListView.as_view(), name='hsk-list'),

]
