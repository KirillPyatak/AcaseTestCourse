# models.py
from django.db import models
#уровень сложности курса
class Difficulty(models.Model):
    level = models.CharField(max_length=50, choices=[('A1','A2'),('B1','B2')])
#Язык курса
class Language(models.Model):
    name = models.CharField(max_length=50)
#цены
class Price(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)

#основная информация на странице создание курса
class Course(models.Model):
    #Изображения для курса
    cover_image = models.ImageField(upload_to='course_covers/')
    #Название курса
    title = models.CharField(max_length=255)
    #Описание курса
    description = models.TextField()
    #Программа курса
    program = models.TextField()
    #Что вы изучите
    what_you_learn = models.TextField()
    #Бонус
    bonus = models.TextField()
    #Сложность
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    #Язык
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    #Цены
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    #Модули курса
    modules = models.PositiveIntegerField()

    lessons = models.PositiveIntegerField()
