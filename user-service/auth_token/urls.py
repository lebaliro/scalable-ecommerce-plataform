from django.urls import path

from auth_token import views

app_name = 'auth_token'

urlpatterns = [
    path('token/', views.GetTokenApiView.as_view(), name='get_token'),
    path('token/refresh/', views.RefreshTokenApiView.as_view(), name='refresh_token')
]
