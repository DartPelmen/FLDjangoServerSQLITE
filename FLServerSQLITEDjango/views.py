import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from FLServerSQLITEDjango import models
from FLServerSQLITEDjango.models import Table1


# View: по факту методы, описывающие,
# что должен получить пользователь при обращении по определенным ссылкам на сайте.
def getAll(request):
    output = []
    out = models.Table1.objects.filter(id=1).values()
    return JsonResponse({"data1": out[0]['data1']})


@csrf_exempt
def insertRow(request):
    if request.method == 'POST':
        row = json.loads(request.body)
        if request.body is None:
            return JsonResponse({"status": "INVALID INPUT"})
        origin = models.Table1.objects.filter(id=1).values()[0]
        origin['data1'] = row['data2']
        table = Table1(id=1, data1=origin['data1'], data2=origin['data2'], data3=origin['data3'], data4=origin['data4'])
        table.save()
        return JsonResponse({"status": "OK"})
    else:
        return JsonResponse({"status": "NOT POST"})