import os
from anadolucore.models import Customer

BASE_PATH = os.path.join(os.getcwd(), 'datasets', 'tic2000')
TRAIN_DATA_FILENAME = os.path.join(BASE_PATH, 'ticdata2000.txt')
TEST_DATA_FILENAME = os.path.join(BASE_PATH, 'ticeval2000.txt')
EVAL_FILENAME = os.path.join(BASE_PATH, 'tictgts2000.txt')
def readData(TRAIN_DATA_FILENAME, TEST_DATA_FILENAME, EVAL_FILENAME):
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
trainData, testData = readData(TRAIN_DATA_FILENAME, TEST_DATA_FILENAME, EVAL_FILENAME)

nameList = ["subtype", "number_of_houses", "size_household", "avg_age", "maintype",
            "roman_catholic", "protestant", "other_religion", "no_religion", "married",
            "living_together", "other_relation", "singles", "household_without_children", "household_with_children",
            "high_level_education", "medium_level_education", "lower_level_education", "high_status", "entrepreneur",
            "farmer", "middle_management", "skilled_labourers", "unskilled_labourers", "social_class_a",
            "social_class_b1", "social_class_b2", "social_class_c", "social_class_d", "rented_house",
            "home_owners", "one_car", "two_car", "no_car", "national_health_service",
            "private_health_insurance", "income_less_30", "income_30_45", "income_45_75", "income_75_122",
            "income_more_123", "average_income", "purchasing_power_class", "private_insurance", "firms_insurance",
            "agriculture_insurance", "car_policies", "van_policies", "motorcycle_policies", "lorry_policies",
            "trailer_policies", "tractor_policies", "agricultural_machines_policies", "moped_policies", "life_insurances",
            "private_accident_insurance", "family_accidents_insurance", "disability_insurance", "fire_policies", "surfboard_policies",
            "boat_policies", "bicycle_policies", "property_insurance_policies", "social_security_insurance_policies", "number_private_insurance",
            "number_firms_insurance", "number_agriculture_insurance", "number_car_policies", "number_van_policies", "number_motorcycle_policies",
            "number_lorry_policies", "number_trailer_policies", "number_tractor_policies", "number_agricultural_machines_policies", "number_moped_policies",
            "number_life_insurances", "number_private_accident_insurance", "number_family_accidents_insurance", "number_disability_insurance", "number_fire_policies",
            "number_surfboard_policies", "number_boat_policies", "number_bicycle_policies", "number_property_insurance_policies", "number_social_security_insurance_policies",
            "number_mobile_home_policies"
            ]
from anadolucore.choices import L0, L1, L2, L3, L4

for index, row in enumerate(trainData):
    dataDict = {"index": index, "isTest": False}
    for i, key in enumerate(nameList):
        row[i] = int(row[i])
        if i == 0:
            dataDict[key] = L0(row[i])
        elif i == 3:
            dataDict[key] = L1(row[i])
        elif i == 4:
            dataDict[key] = L2(row[i])
        elif 5 <= i and i <= 42:
            dataDict[key] = L3(row[i])
        elif 43 <= i and i <= 63:
            dataDict[key] = L4(row[i])
        else :
            dataDict[key] = row[i]
    c = Customer(**dataDict)
    c.save()

for index, row in enumerate(testData):
    dataDict = {"index": index, "isTest": False}
    for i, key in enumerate(nameList):
        row[i] = int(row[i])
        if i == 0:
            dataDict[key] = L0(row[i])
        elif i == 3:
            dataDict[key] = L1(row[i])
        elif i == 4:
            dataDict[key] = L2(row[i])
        elif 5 <= i and i <= 42:
            dataDict[key] = L3(row[i])
        elif 43 <= i and i <= 63:
            dataDict[key] = L4(row[i])
        else:
            dataDict[key] = row[i]
    c = Customer.objects.create(**dataDict)
    c.save()
