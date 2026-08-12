from django.urls import path

from .views import (
    PipelineListView,
    ProductionPipelineView,
    MetricsView,
)

urlpatterns = [
    path(
        "pipelines/",
        PipelineListView.as_view(),
        name="pipeline-list",
    ),

    path(
        "pipelines/production/",
        ProductionPipelineView.as_view(),
        name="production-pipelines",
    ),

    path(
        "metrics/",
        MetricsView.as_view(),
        name="metrics",
    ),
]