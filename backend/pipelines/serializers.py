from rest_framework import serializers
from .models import PipelineRun


class PipelineRunSerializer(serializers.ModelSerializer):

    class Meta:
        model = PipelineRun
        fields = "__all__"