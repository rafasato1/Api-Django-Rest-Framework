from rest_framework import serializers
from school.grades.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [ 'id','first_name', 'last_name','age']