import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import CleanTextForm
from .models import CleaningRecord
from .services import process_text


def home(request):
    form = CleanTextForm(request.POST or None)
    result = None

    if request.method == "POST" and form.is_valid():
        result = process_text(form.cleaned_data["text"])

    return render(request, "cleaner/home.html", {"form": form, "result": result})


def history(request):
    records = CleaningRecord.objects.all()[:20]
    return render(request, "cleaner/history.html", {"records": records})


@require_http_methods(["POST"])
def api_clean(request):
    try:
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": 'Request body must be JSON like {"text": "..."}.'},
            status=400,
        )

    if not isinstance(payload, dict) or "text" not in payload:
        return JsonResponse(
            {"error": 'Missing "text" field. Send JSON like {"text": "..."}.'},
            status=400,
        )

    text = payload.get("text")
    if text is None or not str(text).strip():
        return JsonResponse(
            {"error": '"text" is required and cannot be empty.'},
            status=400,
        )

    return JsonResponse(process_text(str(text)))
