from rest_framework import serializers
from .models import Course, Deliverable, Student, Supplier, Skill, EnrolledIn, PrerequisitCourses
from rest_framework.reverse import reverse



class PrerequisitCoursesSerializer(serializers.ModelSerializer):     
    class Meta:
        model = PrerequisitCourses
        fields = '__all__'


class EnrolledInSerializer(serializers.ModelSerializer):     
    class Meta:
        model = EnrolledIn
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Skill
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Supplier
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Student
        fields = '__all__'

class DeliverableSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Deliverable
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    Deliverable_course = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )
    
    class Meta:
        model = Course
        fields = '__all__'
