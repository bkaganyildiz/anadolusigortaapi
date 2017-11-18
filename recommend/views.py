# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os
import numpy as np
import pandas as pd
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from helper import recommend_utils

BASE_PATH = os.path.join("datasets", "tic2000")

TEST_DATA = None
TRAIN_DATA = None

@api_view(['GET',])
def getAllFields(request):
    """
    Retrieve, update or delete a code snippet.
    """
    retValues = readDescriptions()

    ret = json.dumps(retValues)
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

def readData():
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

    TRAIN_DATA = pd.DataFrame(data=trainData)
    TEST_DATA = pd.DataFrame(data=testData)
