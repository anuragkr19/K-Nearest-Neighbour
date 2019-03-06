import csv
import os
import math
import operator

'''
External Reference used
https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
https://realpython.com/welcome/
'''

#Loading Training data sets from inputdata.txt file
def loadDataSet():
    dataPoints = []
    fileh = open(os.getcwd() + "//code//inputdata.txt",'r')
    try:
        csv_reader = csv.reader(fileh,delimiter=',')
        for row in csv_reader:
            tempList = []
            tempList.append(float(row[0])) # Height
            tempList.append(float(row[1])) # Weight
            tempList.append(float(row[2])) # Age
            tempList.append(row[3]) # Class Label
            dataPoints.append(tempList)
    except:
        pass
    fileh.close()
    return dataPoints

#Loading Test data sets from sampledata.txt file
def loadInputData():
    sampleData = []
    fileSecondh = open(os.getcwd() + "//axk1923_hw1//code//sampledata.txt")

    try:
        csv_reader = csv.reader(fileSecondh,delimiter=',')
        for row in csv_reader:
            tempList = []
            tempList.append(float(row[0])) # Height
            tempList.append(float(row[1])) # Weight
            tempList.append(float(row[2])) # Age
            #tempList.append(row[3]) # Class Label
            sampleData.append(tempList)
    except:
        pass
    fileSecondh.close()
    return sampleData


#Main fucntion contains main entry for the programme
def mainFunc():

    inputDataList = loadDataSet()
    sampleDataList  = loadInputData()
    kValues = [1,3,5]
    count = 0
    for i in range(0,len(sampleDataList)):
        count+=1
        #find distance of each input point with available training set for each feature
        resultLabel = []
        #neighbours = []
        for j in range(len(kValues)):
            #get neighbours
            neighbours = getNeighbour(kValues[j],sampleDataList[i],inputDataList)
            resultLabel.append(neighbours)

        print sampleDataList[i]
        formatter = "For k = %r , class is %r"
        for k in range(0,len(resultLabel)):
            print formatter % (kValues[k],resultLabel[k])
        print " "


#calculate euclidean distance between testdata and each dataPoints of training Data
def getEuclideanDistance(testData,trainingData,length):
    distance = 0
    for x in range(length):
        distance+= (testData[x] - trainingData[x])**2
    return math.sqrt(distance)


#Result label for the maximum occurrring class type based on value for k
def getNeighbour(k,testInstance,trainingList):
    distances = []
    length  = len(testInstance) - 1
    tempList = []
    for x in range(len(trainingList)):
        trainList = trainingList[x]
        sqrTerm  = 0
        for j in range(len(testInstance)):
            sqrTerm += ((testInstance[j] - trainList[j])**2)

        squareRootTerm = math.sqrt(sqrTerm)
        tempList.append(squareRootTerm)
        distances.append(squareRootTerm)

    newList = []
    newList = sorted(range(len(distances)),key = lambda k: distances[k])

    neighbours = []
    trainInListIndex = 0
    trainInListIndex
    for i in range(k):
        trainInListIndex = newList[i]
        label = trainingList[trainInListIndex][3]
        neighbours.append(label)
    return min([sublist[-1] for sublist in neighbours])


#calling main function
mainFunc()
