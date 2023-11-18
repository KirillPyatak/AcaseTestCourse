from django.contrib import admin
from .models import Course, Difficulty, Language, Price

class DifficultyAdmin(admin.ModelAdmin):
    list_display = ('level',)

admin.site.register(Difficulty, DifficultyAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Language, LanguageAdmin)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('amount', 'currency')

admin.site.register(Price, PriceAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'language', 'price', 'modules', 'lessons')

admin.site.register(Course, CourseAdmin)
