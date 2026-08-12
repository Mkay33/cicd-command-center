from django.contrib import admin

from .models import PipelineRun


@admin.register(PipelineRun)
class PipelineRunAdmin(admin.ModelAdmin):

    list_display = (
        "pipeline_name",
        "environment",
        "status",
        "ci_provider",
        "started_at",
    )

    list_filter = (
        "environment",
        "status",
        "ci_provider",
    )

    search_fields = (
        "pipeline_name",
        "branch",
        "commit_sha",
    )

# Register your models here.
