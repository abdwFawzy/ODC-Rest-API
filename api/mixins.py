from rest_framework import permissions
from .permissions import IsInstructor, IsAdmin

class InstructorPermissionMixin():
    permession_classes = [permissions.IsAdminUser, IsInstructor]
class CoursePermissionMixin():
    permession_classes = [permissions.IsAdminUser, IsAdmin]
    