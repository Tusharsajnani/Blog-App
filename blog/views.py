from rest_framework import viewsets
from blog.models import Student
from .serializer import Studentserializer
from django.http  import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#viewset
#serializer.serializer
#use postgres database

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Student
from .serializer import Studentserializer


@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    serializer = Studentserializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_student(request):
    serializer = Studentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_student_by_id(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = Studentserializer(student)
    return Response(serializer.data)

@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = Studentserializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({'message': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)
