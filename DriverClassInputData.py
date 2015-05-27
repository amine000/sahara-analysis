from readingInput import openFileAndRead, strings, rowObjects, DataPoint, getRowObjects, getStrings, getGoodDataPoints, goodDataArray

pValues = []
tValues = []


def driverMethod():
	openFileAndRead()  
	print len(getRowObjects())
	print getGoodDataPoints()
	fittingDataArray = goodDataArray[:10000]
	print "We have " + str(len(fittingDataArray)) + " points"
	testingArray = goodDataArray[10000:]
	print "we have " + str(len(testingArray)) +  " points in the testing array"
	
def findAverage():
	totalP = 0
	totalT = 0
	for datapoint in goodDataArray:
		totalP += int(datapoint.valuesArray[6]) 
		totalT += int(datapoint.valuesArray[11])
	avgP = totalP/len(goodDataArray)
	avgT = totalT/len(goodDataArray)
	print "the average P is", str(avgP) + " the average t is", str(avgT)

driverMethod()
findAverage()