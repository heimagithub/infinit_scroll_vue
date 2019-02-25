from django.shortcuts import render

# Create your views here.

import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_msg(request):
    try:
        print('======init_msg======')
        index = json.loads(request.body.decode('utf-8'))['index']

        msg = []
        for i in range(1,31):
            msg.append(
                {
                    "body": i+30*index,
                }
            )

        return JsonResponse({'success': True, "msg": msg})

    except Exception as e:
        print(e)

