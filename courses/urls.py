from django.urls import path
from .views import (
    CategoryListAPIView, CategoryDetailAPIView,
    CourseListAPIView, CourseDetailAPIView,
    SubscribeCourseAPIView, SubscriptionListAPIView
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('courses/<int:pk>/subscribe/', SubscribeCourseAPIView.as_view(), name='course-subscribe'),
    path('my-subscriptions/', SubscriptionListAPIView.as_view(), name='my-subscriptions'),
]