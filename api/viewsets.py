from rest_framework import viewsets, mixins, generics
from url_filter.integrations.drf import DjangoFilterBackend
from.models import *
from .serializers import *

from rest_framework import filters
from .mixins import InstructorPermissionMixin, CoursePermissionMixin
class CourseViewSet(viewsets.ModelViewSet, CoursePermissionMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_fields = '__all__'


class PrerequisitCoursesViewSet(viewsets.ModelViewSet):     
    queryset = PrerequisitCourses.objects.all()
    serializer_class = PrerequisitCourses
    lookup_field = 'pk'
    filter_fields = '__all__'
class EnrolledInViewSet(viewsets.ModelViewSet):     
    queryset = EnrolledIn.objects.all()
    serializer_class = EnrolledIn
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
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    
class DeliverableViewSet(viewsets.ModelViewSet):     
    queryset = Deliverable.objects.all()
    serializer_class = DeliverableSerializer
    lookup_field = 'pk'
    filter_fields = '__all__'