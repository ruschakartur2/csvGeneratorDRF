from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateUserAPIView.as_view(), name='create'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),

]