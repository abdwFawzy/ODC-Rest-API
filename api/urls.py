from django.urls import path
from .viewsets import CourseViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .views import api_home, Course_detail_view, Course_list_create_view, Course_Update_view, Course_destroy_view

urlpatterns = [
    
    path('Course/<int:pk>/', CourseViewSet, name='CourseViewSet-list'),
    path('Course/', CourseViewSet, name='CourseViewSet-detail'),
    path('Course/<int:pk>/update', CourseViewSet, name='CourseViewSet-update'),
    path('Course/<int:pk>/delete', CourseViewSet, name='CourseViewSet-delete')
]