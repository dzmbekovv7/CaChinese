
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vocabulary/', include('vocabulary.urls')),
    path('api/flashcards/', include('flashcards.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/listening/', include('listening.urls')),
]
