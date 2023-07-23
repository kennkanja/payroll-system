from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length = 100)
    unit_code = models.CharField(max_length = 100)
    course = models.CharField(max_length = 50)
    department  =  models.CharField(max_length = 100)
    exam_type = models.CharField(max_length = 100)
       

    def __str__(self):
        return self.name
    

class Lecturer(models.Model):
    name = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)  
    cost = models.IntegerField()
    quantity =  models.IntegerField()
    

    def __str__(self):
        return self.name