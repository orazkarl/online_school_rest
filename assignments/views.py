from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Assignment, AssignmentTaskFile, AssignmentAnswer
from .serializers import AssignmentCreateSerializer, AssignmentListSerializer


class AssignmentCreateView(generics.CreateAPIView):
    serializer_class = AssignmentCreateSerializer


class AssignmentListView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer



