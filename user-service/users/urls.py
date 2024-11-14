from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('user/', views.UserCreateApiView.as_view(), name='create'),
    path('user/<int:pk>/', views.UserDetailApiView.as_view(), name='detail')
]