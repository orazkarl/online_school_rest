from rest_framework import serializers

from .models import Assignment, AssignmentAnswer, AssignmentTaskFile


class AssignmentListSerializer(serializers.ModelSerializer):
    """List of assigments"""

    class Meta:
        model = Assignment
        fields = "__all__"

class AssignmentCreateSerializer(serializers.ModelSerializer):
    """Create assignment"""

    class Meta:
        model = Assignment
        fields = "__all__"

