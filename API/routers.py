from api.viewsets import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('Student', CourseViewSet, basename='Courses')

router.register('Skill', SkillViewSet, basename='Skills')

router.register('EnrolledIn', EnrolledInViewSet, basename='EnrolledIns')

router.register('PrerequisitCourses', PrerequisitCoursesViewSet, basename='PrerequisitCoursess')

router.register('Supplier', SupplierViewSet, basename='Suppliers')

router.register('Student', StudentViewSet, basename='Students')

router.register('Course', CourseViewSet, basename='Courses')


router.register('Deliverable', DeliverableViewSet, basename='Deliverables')

urlpatterns = router.urls