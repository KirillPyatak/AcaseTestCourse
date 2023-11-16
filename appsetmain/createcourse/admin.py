from django.contrib import admin
from .models import Course
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(Course)