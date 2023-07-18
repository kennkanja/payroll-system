from django.urls import include, path

from rest_framework import  routers

from payroll.views import  ExamViewSet, LecturerViewSet

router = routers.DefaultRouter()
router.register(r'exam', ExamViewSet)
router.register(r'lecturer',LecturerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]