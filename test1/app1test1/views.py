import json
from django.shortcuts import render
from .models import Cities
from .serializers import citySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
#how to bring single data 

def cityView(request):
    citydetails = Cities.objects.get(id=1)
    cityser = citySerializer(citydetails)
    cityjsondata = JSONRenderer().render(cityser.data)
    return HttpResponse(cityjsondata,content_type='application/json')

def cityAllView(request):
    citydetails = Cities.objects.all()
    cityser = citySerializer(citydetails,many=True)
    return JsonResponse(cityser.data,safe=False)