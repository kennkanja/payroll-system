from rest_framework import serializers

from payroll.models import  Exam , Lecturer

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('name','unit_code','course', 'department','exam_type')



class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('name', 'phone_no', 'exam','cost','quality')

    