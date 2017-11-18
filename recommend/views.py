# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os

import django_filters
import numpy as np
import pandas as pd
from .serializers import RecommendationResultSerializer
from .models import RecommendationResult
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from helper import recommend_utils
from anadolucore.util import get_matrix_data

BASE_PATH = os.path.join("datasets", "tic2000")

TEST_DATA = None
TRAIN_DATA = None

class RecommendationList(generics.ListCreateAPIView):
    queryset = RecommendationResult.objects.all()
    serializer_class = RecommendationResultSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

class RecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecommendationResult.objects.all()
    serializer_class = RecommendationResultSerializer

@api_view(['GET',])
def getAllFields(request):
    """
    Retrieve, update or delete a code snippet.
    """
    retValues = readDescriptions()

    ret = json.dumps(retValues)
    return Response(ret)

@api_view(['GET',])
def getPolicyFields(request):
    """
    Retrieve, update or delete a code snippet.
    """
    retValues = readDescriptions()

    ret = json.dumps(retValues[64:])
    return Response(ret)

@api_view(['POST',])
def getCorMatrix(request):
    body = request.body
    body = json.loads(body)
    readData()

    x_list = map(lambda x: x['id'], body['first'])
    y_list = map(lambda x: x['id'], body['second'])

    ret = recommend_utils.getCorrelationMatrix(TRAIN_DATA, x_list, y_list)

    return Response(json.dumps({'picture': ret}))

@api_view(['POST',])
def getDistMatrix(request):
    body = request.body
    body = json.loads(body)
    readData()

    x_id = body['first']['id']
    y_id = body['second']['id']
    # x_list = map(lambda x: x['id'], body['first'])
    # y_list = map(lambda x: x['id'], body['second'])
    # x_id = x_list[0]
    # y_id = y_list[0]

    descriptions = readDescriptions()
    descriptions = map(lambda x: x['label'], descriptions)
    ret = recommend_utils.getViolinPlot(TRAIN_DATA, descriptions, x_id, y_id)

    return Response(json.dumps({'picture': ret}))

@api_view(['POST',])
def getCountMatrix(request):
    body = request.body
    body = json.loads(body)
    readData()

    print "body: ", body
    x_id = body['field']['id']

    ret = recommend_utils.getCountPlot(TRAIN_DATA, x_id)

    return Response(json.dumps({'picture': ret}))

@api_view(['POST',])
def getAssociationRules(request):
    body = request.body
    body = json.loads(body)
    print "11111"
    readData()
    print "22222"

    print "body: ", body
    lhs = map(lambda x: x['id'], body['first'])
    minSupport = float(body['minSupport'])
    minConfidence = float(body['minConfidence'])
    descriptions = readDescriptions()

    ret = recommend_utils.associationFinder(TRAIN_DATA, lhs, minSupport)
    for item in ret:
        item['dest'] = descriptions[item['dest']]["label"]
        item['source'] = map(lambda x: descriptions[x]["label"], item['source'])
        item['confidence'] = "%.3f" % item['confidence']
        item['support'] = "%.3f" % item['support']

    ret = filter(lambda x: x['confidence'] >= minConfidence, ret)
    return Response(json.dumps({'associations': ret}))

@api_view(['GET',])
def predictionSystem(request):
    body = request.body
    readData(False)

    score = recommend_utils.predictionSystem(TRAIN_DATA, TEST_DATA)

    return Response(json.dumps({'score': score}))


def readDescriptions():
    FILE_NAME = os.path.join(BASE_PATH, "labels.txt")
    f = open(str(FILE_NAME), str('rb'))
    retValues = []
    for line in f.readlines():
        line = unicode(line)
        line = line.strip()
        if not line:
            continue
        arr = line.split(' ')
        id = int(arr[0]) - 1
        label = ' '.join(arr[2:])
        retValues.append({'id': id, 'label': label})
    return retValues

def readData(getNumpy=True):
    '''
    reads data and returns train and test data
    '''
    global TEST_DATA
    global TRAIN_DATA
    global BASE_PATH
    TRAIN_DATA_FILENAME = str(os.path.join(BASE_PATH, 'ticdata2000.txt'))
    TEST_DATA_FILENAME = str(os.path.join(BASE_PATH, 'ticeval2000.txt'))
    EVAL_FILENAME = str(os.path.join(BASE_PATH, 'tictgts2000.txt'))

    f = open(TRAIN_DATA_FILENAME, 'rb')
    trainData = []
    for line in f.readlines():
        arr = line.strip().split('\t')
        arr = map(lambda x: int(x), arr)
        trainData.append(arr)
    f.close()

    f = open(TEST_DATA_FILENAME, 'rb')
    testData = []
    for line in f.readlines():
        arr = line.strip().split('\t')
        arr = map(lambda x: int(x), arr)
        testData.append(arr)
    f.close()

    f = open(EVAL_FILENAME, 'rb')
    for index, val in enumerate(f.readlines()):
        val = int(val)
        testData[index].append(val)
    f.close()

    # trainData = get_matrix_data(False)
    # testData = get_matrix_data(True)
    if getNumpy:
        TRAIN_DATA = pd.DataFrame(data=trainData)
        TEST_DATA = pd.DataFrame(data=testData)
    else:
        TRAIN_DATA = trainData
        TEST_DATA = testData
