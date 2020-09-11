from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from .apps import PredictionConfig

# Create your views here.
@api_view(['GET', 'POST'])
def api_add(request):
    sum = 0
    response_dict = {}
    if request.method == 'GET':
        # Do nothing
        pass
    elif request.method == 'POST':
        # Add the numbers
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
    return Response(response_dict, status=status.HTTP_201_CREATED)

class Add_Values(APIView):
    def post(self, request, format=None):
        sum =0
        #add the numbers
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum" : sum}
        return Response(response_dict, status=status.HTTP_201_CREATED)    


class IRIS_Model_Predict(APIView):
    def post(self, request, format=None):
        data = request.data
        keys = []
        values = []
        for key in data:
            keys.append(key)
            values.append(data[key])
        X = pd.Series(values).to_numpy().reshape(1,-1)
        loaded_classifier = PredictionConfig.classifier
        y_pred = loaded_classifier.predict(X)
        y_pred = pd.Series(y_pred)
        target_map = {0:'setosa', 1:'versicolor', 2:'virginica'}
        y_pred = y_pred.map(target_map).to_numpy()
        response_dict = {"Prediced Iris Species": y_pred[0]}
        return Response(response_dict, status=200)