from rest_framework import generics
from .models import Course, Difficulty, Language, Price
from .serializers import CourseSerializer, DifficultySerializer, LanguageSerializer, PriceSerializer
from django.core.cache import cache
from rest_framework import generics
from django.db import transaction
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all().select_related('difficulty', 'language', 'price')
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all().select_related('difficulty', 'language', 'price')
    serializer_class = CourseSerializer
#Добавил кеширование для сложности
#если данные не найдены в кэше, они извлекаются из базы данных, кэшируются и возвращаются. При последующих запросах данные будут взяты из кэша
from django.db import transaction

class DifficultyListCreateView(generics.ListCreateAPIView):
    serializer_class = DifficultySerializer

    @transaction.atomic
    def get_queryset(self):
        cache_key = 'difficulty_list'
        difficulties = cache.get(cache_key)
        if not difficulties:
            difficulties = Difficulty.objects.all()
            cache.set(cache_key, difficulties)
        return difficulties

    def perform_create(self, serializer):
        with transaction.atomic():
            instance = serializer.save()
            # Очистить кэш при добавлении новой сложности
            cache_key = 'difficulty_list'
            cache.delete(cache_key)

class DifficultyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer

class LanguageListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class PriceListCreateView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class PriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
