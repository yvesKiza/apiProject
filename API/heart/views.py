from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import hospital
from .serializers import hospitalSerializer, PredictionSerializer
from django.shortcuts import render
from .apps import Predictator

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views

# Create your views here.

@csrf_exempt
def hospital_list(request):
    """
    List all code hospita;s, or create a new hospita;.
    """
    if request.method == 'GET':
       hospitals=hospital.objects.all()
       serializer=hospitalSerializer(hospitals, many=True)
       return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = hospitalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def hospital_detail(request, pk):
    """
    Retrieve, update or delete a code hospital.
    """
    
    try:
        Hospital = hospital.objects.get(pk=pk)
    except hospital.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = hospitalSerializer(Hospital)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = hospitalSerializer(Hospital, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Hospital.delete()
        return HttpResponse(status=204)
    
class predict(views.APIView):
       def post(self, request):
         
        content=request.data
        serializer=PredictionSerializer(data=content)
        # results=return_prediction(content)
        # return Response(results[0], status=status.HTTP_200_OK)
        # return Response(results)
        if serializer.is_valid():
            results=return_prediction(serializer.data)
            return Response(results[0], status=200)

        return JsonResponse(serializer.errors, status=422)
     



def return_prediction(sample_json):
    age=sample_json['age']
    sex=sample_json['sex']
    cp=sample_json['cp']
    trestbps=sample_json['trestbps']
    chol=sample_json['chol']
    fbs=sample_json['fbs']
    restecg=sample_json['restecg']
    thalach=sample_json['thalach']
    exang=sample_json['exang']
    oldpeak=sample_json['oldpeak']
    slope=sample_json['slope']
    ca=sample_json['ca']
    thal=sample_json['thal']
    
    predict_disease=[[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang, oldpeak, slope, ca, thal]]
    predict_disease=Predictator.scaler.transform(predict_disease)
    return Predictator.model.predict(predict_disease)
