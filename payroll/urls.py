from django.urls import include, path

from rest_framework import  routers

from payroll.views import  ExamViewSet, HomePageView, LecturerViewSet

router = routers.DefaultRouter()
router.register(r'exam', ExamViewSet)
router.register(r'lecturer',LecturerViewSet)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('', include(router.urls)),
]