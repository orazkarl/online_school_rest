from rest_framework import serializers

from .models import Discipline


class DisciplineListSerializer(serializers.ModelSerializer):
    """ List of disciplines"""

    class Meta:
        model = Discipline
        fields = ('__all__')


class DisciplineDetailSerializer(serializers.ModelSerializer):
    """ Detail of discipline"""

    class Meta:
        model = Discipline
        fields = ('__all__')