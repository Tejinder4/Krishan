from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .models import Teacher
from .serializers import StudentSerializer
from .serializers import TeacherSerializer


class StudentList(APIView):

    def get(self, request):
        Student1 = Student.objects.all()
        serializer =StudentSerializer(Student1, many= True)
        return Response(serializer.data)

    def post(self):
        pass

class TeacherList(APIView):

    def get(self, request):
        Teacher1 = Teacher.objects.all()
        serializer = TeacherSerializer(Teacher1, many= True)
        return Response(serializer.data)

    def post(self):
        pass

