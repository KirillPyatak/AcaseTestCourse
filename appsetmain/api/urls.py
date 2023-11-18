# urls.py
from django.urls import path
from .views import CourseListCreateView, CourseDetailView, DifficultyListCreateView, DifficultyDetailView, LanguageListCreateView, LanguageDetailView, PriceListCreateView, PriceDetailView

urlpatterns = [
    path('api/courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('api/difficulties/', DifficultyListCreateView.as_view(), name='difficulty-list-create'),
    path('api/difficulties/<int:pk>/', DifficultyDetailView.as_view(), name='difficulty-detail'),
    path('api/languages/', LanguageListCreateView.as_view(), name='language-list-create'),
    path('api/languages/<int:pk>/', LanguageDetailView.as_view(), name='language-detail'),
    path('api/prices/', PriceListCreateView.as_view(), name='price-list-create'),
    path('api/prices/<int:pk>/', PriceDetailView.as_view(), name='price-detail'),
]
