from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'name:{self.name}'
    

class Supplier(models.Model):
    name = models.CharField(max_length=20)
    paid_money = models.FloatField()
    rest_money = models.FloatField()
    total_money = models.FloatField()
    

    def __str__(self):
        return f'name:{self.name}, paid_money: {self.paid_money}, total_money: {self.total_money}, rest_money: {self.rest_money}'
    


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    experience = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    student_skills = models.ManyToManyField(Skill, related_name='students')
    
    def __str__(self):
        return f'title: {self.title}, gender:{self.gender}name:{self.name}'
    

class Course(models.Model):
    name = models.CharField(max_length=50)
    course_skills = models.ManyToManyField(Skill, related_name='courses')
    prerequisit_skills = models.ManyToManyField(Skill, related_name='pre_courses')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField(Student, through='EnrolledIn')
    def __str__(self):
        return f'name: {self.name}, course_skills:{self.course_skills}supplier:{self.supplier}'
   


class PrerequisitCourses(models.Model):
    course_name = models.CharField(max_length=20)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='pre_courses')


    def __str__(self):
        return f'course_name:{self.course_name}'


class Deliverable(models.Model):
    name = models.CharField(max_length=30)
    deliverable_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='deliverables')
    
    def __str__(self):
        return f'name:{self.name}'
    

class EnrolledIn(models.Model):
    start_date = models.DateField(default=datetime.date.today(), blank=True)
    end_date = models.DateField(blank=True)
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
