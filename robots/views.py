import json

from django.http import JsonResponse
from .models import Robot
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def created_robots(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        serial = body.get('serial')
        model = body.get('model')
        version = body.get('version')
        created = body.get('created')
        if len(serial) > 5 or len(model) > 2 or len(version) > 2:
            return JsonResponse({'error': 'no valid'}, status=400)
        if Robot.objects.filter(serial=serial, model=model, version=version).exists():
            return JsonResponse({'error':'Already exists'})
        if not serial or not model or not version:
            return JsonResponse({"error":"Missing required fields"}, status=400)
        robot = Robot.objects.create(
            serial=serial,
            model=model,
            version=version,
            created=created
        )
        return JsonResponse({'message': f'Created {robot} '})

