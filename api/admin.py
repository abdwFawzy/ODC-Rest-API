from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(EnrolledIn)
admin.site.register(Deliverable)
admin.site.register(PrerequisitCourses)
admin.site.register(Supplier)


