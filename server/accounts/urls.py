from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home),
    path('register/', views.register, name="register_user"),
    path('create_user/', views.create_user_success),
    path('logout/', views.log_out, name="sign_user_out"),
]
