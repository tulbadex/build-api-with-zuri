from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import studentSerializers

# Create your views here.
# Generic views, DRF has 4 views

# making a post request
class studentViews(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializers

    """ def Create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data) """

    """ def perform_create(self, serializer):
        return super().peform_create(serializer) """

""" @api_view(['POST'])
def create_student(request):
    student = Student.objects.all()
    serializer = studentSerializers(student, many=True)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) """

class getStudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializers

class updateStudentView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializers

class deleteStudentView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializers