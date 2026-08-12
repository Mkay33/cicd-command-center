from datetime import timedelta

from django.db.models import Avg

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PipelineRun
from .serializers import PipelineRunSerializer


class PipelineListView(APIView):
    """
    GET /api/pipelines/
    Returns all pipeline runs.
    """

    def get(self, request):
        pipelines = PipelineRun.objects.all().order_by("-started_at")

        serializer = PipelineRunSerializer(
            pipelines,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class ProductionPipelineView(APIView):
    """
    GET /api/pipelines/production/
    Returns only production pipeline runs.
    """

    def get(self, request):
        pipelines = PipelineRun.objects.filter(
            environment="Production"
        ).order_by("-started_at")

        serializer = PipelineRunSerializer(
            pipelines,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class MetricsView(APIView):
    """
    GET /api/metrics/
    Returns dashboard metrics.
    """

    def get(self, request):

        total = PipelineRun.objects.count()

        successful = PipelineRun.objects.filter(
            status="SUCCESS"
        ).count()

        failed = PipelineRun.objects.filter(
            status="FAILED"
        ).count()

        running = PipelineRun.objects.filter(
            status="RUNNING"
        ).count()

        # Failure rate
        if total > 0:
            failure_rate = round(
                (failed / total) * 100,
                2
            )
        else:
            failure_rate = 0

        # Average build duration
        average_duration = PipelineRun.objects.aggregate(
            average=Avg("duration")
        )["average"]

        if average_duration:
            average_duration_seconds = int(
                average_duration.total_seconds()
            )
        else:
            average_duration_seconds = 0

        # Deployment frequency
        today = PipelineRun.objects.filter(
            started_at__date=__import__("datetime").date.today()
        ).count()

        return Response(
            {
                "total_builds": total,
                "successful_builds": successful,
                "failed_builds": failed,
                "running_builds": running,
                "failure_rate": failure_rate,
                "average_build_duration_seconds":
                    average_duration_seconds,
                "deployments_today": today,
            },
            status=status.HTTP_200_OK,
        )
