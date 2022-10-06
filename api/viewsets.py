from rest_framework import viewsets, mixins
from.models import *
from .serializers import *

from .mixins import InstructorPermissionMixin, CoursePermissionMixin
class CourseViewSet(viewsets.ModelViewSet, CoursePermissionMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'



class PrerequisitCoursesViewSet(viewsets.ModelViewSet):     
    queryset = PrerequisitCourses.objects.all()
    serializer_class = PrerequisitCourses
    lookup_field = 'pk'

class EnrolledInViewSet(viewsets.ModelViewSet):     
    queryset = EnrolledIn.objects.all()
    serializer_class = EnrolledIn
    lookup_field = 'pk'

class SkillViewSet(viewsets.ModelViewSet):     
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'pk'

class SupplierViewSet(viewsets.ModelViewSet):     
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = 'pk'

class StudentViewSet(viewsets.ModelViewSet):     
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    
class DeliverableViewSet(viewsets.
ModelViewSet):     
    queryset = Deliverable.objects.all()
    serializer_class = DeliverableSerializer
    lookup_field = 'pk'
