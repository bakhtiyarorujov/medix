from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UserUpdateView
)


urlpatterns = [
    path('accounts/register', RegisterView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/update', UserUpdateView.as_view(), name='user_update')
]
