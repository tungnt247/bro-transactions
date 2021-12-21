from django.urls import path
from . import views
from trades.views import list


urlpatterns = [
    path('', list, name="homepage"),
    path('register/', views.register, name="register"),
    path('log_out/', views.log_out, name="log_out"),
    path('log_in/', views.log_in, name='log_in')
]
