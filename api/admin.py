from django.contrib import admin

# Register your models here.
from .models import Student, Course, Skill, EnrolledIn, Deliverable, PrerequisitCourses, Supplier, Admin

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(EnrolledIn)
admin.site.register(Deliverable)
admin.site.register(PrerequisitCourses)
admin.site.register(Supplier)
admin.site.register(Admin)
