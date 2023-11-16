from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.prefetch_related('modules__lessons').all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.prefetch_related('modules__lessons').all()
    serializer_class = CourseSerializer
# @method_decorator(login_required, name='dispatch')
# class CourseCreateView(CreateView):
#     model = Course
#     form_class = CourseForm
#     template_name = 'courses/course_create.html'
#     success_url = '/courses/'