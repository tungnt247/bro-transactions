from django.urls import path, include
from trades.views import list

urlpatterns = [
    path('', view=list),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('trades.urls')),
    path('auth/', include('social_django.urls')),
]
