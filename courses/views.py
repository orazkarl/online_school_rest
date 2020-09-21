from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import Discipline
from .serializers import DisciplineListSerializer, DisciplineDetailSerializer


class DisciplineListView(APIView):
    """Output list of disciplines"""

    def get(self, request):
        disciplines = Discipline.objects.filter(is_active=True)
        serializer = DisciplineListSerializer(disciplines, many=True)
        return Response(serializer.data)


class DisciplineDetailView(APIView):
    """Output detail of disciplines"""

    def get(self, request, pk):
        discipline = Discipline.objects.get(id=pk, is_active=True)
        serializer = DisciplineDetailSerializer(discipline)
        return Response(serializer.data)
