from rest_framework import viewsets, mixins, generics
from url_filter.integrations.drf import DjangoFilterBackend
from.models import *
from .serializers import *

from rest_framework import filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'
 
    filter_fields = '__all__'
    #@method_decorator(cache_page(60*60*2))
    #@method_decorator(vary_on_cookie)


class PrerequisitCoursesViewSet(viewsets.ModelViewSet):     
    queryset = PrerequisitCourses.objects.all()
    serializer_class = PrerequisitCoursesSerializer
    lookup_field = 'pk'
    filter_fields = '__all__'
class EnrolledInViewSet(viewsets.ModelViewSet):     
    queryset = EnrolledIn.objects.all()
    serializer_class = EnrolledInSerializer
    lookup_field = 'pk'
    filter_fields = '__all__'

class SkillViewSet(viewsets.ModelViewSet):     
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'pk'
    filter_fields = '__all__'

class SupplierViewSet(viewsets.ModelViewSet):     
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = 'pk'

class StudentViewSet(
    
    viewsets.ModelViewSet
    ):     
    queryset = Student.objects.all()
    #@method_decorator(cache_page(60*60*2))
    #@method_decorator(vary_on_cookie)
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    
class DeliverableViewSet(viewsets.ModelViewSet):     
    queryset = Deliverable.objects.all()
    serializer_class = DeliverableSerializer
    lookup_field = 'pk'
    filter_fields = '__all__'