from django.urls import path, include
from .views import AuthLoginView, AuthLogoutView, AuthStatusView

urlpatterns = [
    path('auth/login/', AuthLoginView.as_view(), name='auth_login'),
    path('auth/logout/', AuthLogoutView.as_view(), name='auth_logout'),
    path('auth/status/', AuthStatusView.as_view(), name='auth_status'),
]