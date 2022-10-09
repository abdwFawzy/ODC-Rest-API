from rest_framework import generics, mixins, permissions, authentication
import json
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CourseSerializer
from .mixins import InstructorPermissionMixin, CoursePermissionMixin
from .models import Course

from .authentication import TokenAuthentication
# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    pass



class CourseListCreateAPIView(
    generics.ListCreateAPIView, 
    InstructorPermissionMixin):    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [authentication.SessionAuthentication]
Course_list_create_view = CourseListCreateAPIView.as_view()


class CourseDetailAPIView(
    generics.RetrieveAPIView, 
    InstructorPermissionMixin):    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

Course_detail_view = CourseDetailAPIView.as_view()


class CourseUpdateAPIView(
    generics.UpdateAPIView,
    InstructorPermissionMixin
    ):    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
Course_Update_view = CourseUpdateAPIView.as_view()


class CourseDestroyAPIView(
    generics.DestroyAPIView, 
    InstructorPermissionMixin):    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
Course_destroy_view = CourseDestroyAPIView.as_view()
