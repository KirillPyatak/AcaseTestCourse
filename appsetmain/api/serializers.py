# serializers.py
from rest_framework import serializers
from .models import Course, Difficulty, Language, Price

class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    # Вместо явного указания каждого поля используем '__all__' пока вывожу всю информацию, думаю, что теги можно будет хранить в кеше
    difficulty = DifficultySerializer()
    language = LanguageSerializer()
    price = PriceSerializer()

    class Meta:
        model = Course
        fields = '__all__'
