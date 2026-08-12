import json
from datetime import timedelta

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from pipelines.models import PipelineRun


@csrf_exempt
def github_webhook(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed"},
            status=405
        )

    try:
        data = json.loads(request.body)

        started_at = timezone.now()
        duration = timedelta(minutes=3)
        completed_at = started_at + duration

        pipeline = PipelineRun.objects.create(
            environment=data.get("environment", "Development"),
            pipeline_name=data.get(
                "pipeline_name",
                "GitHub Pipeline"
            ),
            ci_provider=data.get(
                "ci_provider",
                "GitHub Actions"
            ),
            status=data.get("status", "SUCCESS"),
            commit_sha=data.get("commit_sha", ""),
            branch=data.get("branch", "main"),
            triggered_by=data.get(
                "triggered_by",
                "GitHub Actions"
            ),
            started_at=started_at,
            completed_at=completed_at,
            duration=duration,
            build_url=data.get(
                "build_url",
                "https://github.com"
            ),
        )

        return JsonResponse(
            {
                "message": "GitHub webhook received successfully",
                "pipeline_id": pipeline.id,
            },
            status=201
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON payload"},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )
