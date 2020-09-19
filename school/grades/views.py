from django.shortcuts import render
from school.grades.models import Student
from django.http import HttpResponse
from django.http import JsonResponse
from school.grades.serializers  import StudentSerializer
from rest_framework import viewsets, generics, mixins
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
