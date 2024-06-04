from django.shortcuts import render
from rest_framework import generics
from browser.models import Student
from browser.serializers import StudentsSerializer
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema


class StandardPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5


# Create your views here.
class StudentsValues(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    pagination_class = StandardPagination

#    @extend_schema(
#            request=StudentsSerializer,
#            responses={201: StudentsSerializer},
#            summary='List all students'
#            )


class StudentValues(generics.RetrieveAPIView):
    serializer_class = StudentsSerializer
    queryset = Student.objects.all()


class CreateStudentValues(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class UpdateStudentValues(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class DeleteStudentValues(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
