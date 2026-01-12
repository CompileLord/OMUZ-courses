from django.urls import path
from .views import RegisterUserAPIView, LoginUserAPIView, LogoutUserAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()),
    path('login/', LoginUserAPIView.as_view()),
    path('logout/', LogoutUserAPIView.as_view()),
]