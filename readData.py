import os

BASE_PATH = os.path.join('datasets', 'tic2000')
TRAIN_DATA_FILENAME	= os.path.join(BASE_PATH, 'ticdata2000.txt')
TEST_DATA_FILENAME	= os.path.join(BASE_PATH, 'ticeval2000.txt')
EVAL_FILENAME = os.path.join(BASE_PATH, 'tictgts2000.txt')
def readData():
    '''
        reads data and returns train and test data
    '''
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

    return trainData, testData

	
trainData, testData = readData()