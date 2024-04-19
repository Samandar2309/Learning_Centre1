from django.urls import path, include
from .views import home_view, teacher_list_view, courselist_view, teacher_detail_view, course_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('teachers/', teacher_list_view, name='teacher-list'),
    path('teacher/<int:pk>/', teacher_detail_view, name='teacher-detail'),
    path('courses/', courselist_view, name='course-list'),
    path('course/<int:pk>/', course_detail_view, name='course-detail'),
    path('contact/', include('contact.urls')),
]
