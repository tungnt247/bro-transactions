from django.urls import path, include
from . import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name="homepage"),
    path('register/', views.register, name="register_user"),
    path('logout/', views.log_out, name="sign_user_out"),
]
