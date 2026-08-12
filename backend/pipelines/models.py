from django.db import models


class PipelineRun(models.Model):

    ENVIRONMENTS = [
        ("Development", "Development"),
        ("QA", "QA"),
        ("Staging", "Staging"),
        ("Pre-Production", "Pre-Production"),
        ("Production", "Production"),
    ]

    STATUS_CHOICES = [
        ("SUCCESS", "SUCCESS"),
        ("FAILED", "FAILED"),
        ("RUNNING", "RUNNING"),
    ]

    environment = models.CharField(
        max_length=30,
        choices=ENVIRONMENTS,
    )

    pipeline_name = models.CharField(max_length=100)

    deployment_version = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )

    ci_provider = models.CharField(max_length=50)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
    )

    commit_sha = models.CharField(max_length=50)

    branch = models.CharField(max_length=100)

    triggered_by = models.CharField(max_length=100)

    started_at = models.DateTimeField()

    completed_at = models.DateTimeField()

    duration = models.DurationField()

    build_url = models.URLField()

    def __str__(self):
        return self.pipeline_name
