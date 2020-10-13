from django.db import models

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tname

class Student(models.Model):
    id  = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=100,null=True,blank=True)
    teacher = models.ForeignKey(Teacher, related_name="student_teacher",
                                on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.sname
