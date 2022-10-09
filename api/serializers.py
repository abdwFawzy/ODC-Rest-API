from rest_framework import serializers
from .models import Course, Deliverable, Student, Supplier, Skill, EnrolledIn, PrerequisitCourses
from rest_framework.reverse import reverse



class PrerequisitCoursesSerializer(serializers.ModelSerializer):     
    class Meta:
        model = PrerequisitCourses
        fields = '__all__'



class SkillSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Skill
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Supplier
        fields = '__all__'


class DeliverableSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Deliverable
        fields = '__all__'
 

class EnrolledInSerializer(serializers.ModelSerializer):     
    student = serializers.StringRelatedField(read_only=True)
    course = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = EnrolledIn
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    course_skills  = SkillSerializer(many=True, read_only=True)
    prerequisit_skills = serializers.StringRelatedField(many=True, read_only=True)
    supplier = SupplierSerializer()
    students = EnrolledInSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):     
    student_skills = SkillSerializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'
        