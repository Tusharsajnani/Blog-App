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

@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Student.objects.all()    # get all the students
        serializer = Studentserializer(blogs, many=True)  # serialize them
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = Studentserializer(data=request.data)  # deserialize the incoming data
        if serializer.is_valid():
            serializer.save()  # save the new Student
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Studentserializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Studentserializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response({'message': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)