from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=30)


class Supplier(models.Model):
    name = models.CharField(max_length=20)
    paid_money = models.FloatField()
    rest_money = models.FloatField()
    total_money = models.FloatField()

class Course(models.Model):
    name = models.CharField(max_length=50)
    course_skills = models.ManyToManyField(Skill, related_name='courses')
    prerequisit_skills = models.ManyToManyField(Skill, related_name='pre_courses')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='courses')

class Deliverable(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='deliverables')
    

class PrerequisitCourses(models.Model):
    course_name = models.CharField(max_length=20)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='pre_courses')

class Student(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    experience = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    status = models.BooleanField()
    user_skills = models.ManyToManyField(Skill, related_name='students')
    enrolled_in = models.ManyToManyField(Course, through='EnrolledIn')
    def __str__(self):
        return f'title: {self.title}, gender:{self.gender}name:{self.name}'
    @property
    def courses(self):
        return self.user_skills
class admin(models.Model):
    name  = models.CharField(max_length=50)
    password = models.IntegerField()

class EnrolledIn(models.Model):
    start_date = models.DateField(default=datetime.date.today(), blank=True)
    end_date = models.DateField()
    attendace = models.FloatField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    student_rate = models.FloatField(default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)