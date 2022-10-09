from api.viewsets import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student', StudentViewSet, basename='Students')

router.register('skill', SkillViewSet, basename='Skills')

router.register('enrolledIn', EnrolledInViewSet, basename='EnrolledIns')

router.register('prerequisitCourses', PrerequisitCoursesViewSet, basename='PrerequisitCoursess')

router.register('supplier', SupplierViewSet, basename='Suppliers')


router.register('course', CourseViewSet, basename='Courses')


router.register('deliverable', DeliverableViewSet, basename='Deliverables')

urlpatterns = router.urls