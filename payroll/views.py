from django.shortcuts import render

from rest_framework import viewsets
from django.views.generic import ListView

from payroll.serializers import ExamSerializer, LecturerSerializer
from payroll.models import Exam, Home , Lecturer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class HomePageView(ListView):
    model = Home
    extra_context = {
        "lecturers": Lecturer.objects.all(),
        "exams":Exam.objects.all()
    }
    template_name = "index.html"