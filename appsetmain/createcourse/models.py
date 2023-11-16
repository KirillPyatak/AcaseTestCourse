from django.db import models
import PIL
# модели создание курса.
class Course(models.Model):
    #Название
    title = models.CharField(max_length=255)
    #Описание
    description = models.TextField()
    #Медиа файл
    image_or_video = models.ImageField(upload_to='course_images/', null=True, blank=True)
    #Превью курса
    program_preview = models.TextField()
    #Что вы узнаете
    what_you_will_learn = models.TextField()
    #Бонус
    bonus = models.TextField()

    modules = models.PositiveIntegerField()
    lessons = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=20)
    duration = models.PositiveIntegerField()  # в минутах
    language = models.CharField(max_length=50)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.title