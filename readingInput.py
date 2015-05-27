import csv

strings = []
#contains all data points (about 75k)
rowObjects = []
#contains data-points that have a precipitation (index 6) and a TMAX (index 11), about 12k items
goodDataArray = []


class DataPoint:
	STATION = "" 
	STATION_NAME = ""
	ELEVATION = 0
	LATITUDE = 0
	LONGITUDE = 0
	DATE = 0 
	PRCP = 0
	MeasurementFlag = 0
	QualityFlag = 0
	SourceFlag = 0
	TimeofObservation = 0
	TMAX = 0 
	MeasurementFlag = 0
	QualityFlag = 0 
	SourceFlag = 0 
	TimeofObservation = 0
	TMIN =  0
	MeasurementFlag = 0
	QualityFlag = 0 
	SourceFlag = ""
	TimeofObservation = 0
	valueString = ""
	valueStringClone = ""
	valuesArray = []
	def __init__(self, str):
		self.valueString = str
		self.valueStringClone = str
	def getValueString(self):
		return self.valueString
	def makeArray(self):
		counter = 0
		index = 0
		self.valuesArray = []
		while(counter < 20):
			index = self.valueStringClone.find(',')
			thisValue = self.valueStringClone[0:index]
			#print thisValue
			self.valuesArray.append(thisValue)
			if counter == 0:
				value1 = thisValue
			elif counter == 1:
				value2 = thisValue
			#print thisValue
			self.valueStringClone = self.valueStringClone[index+1:]
			counter+=1
		thisValue = self.valueStringClone[0:]
		#print thisValue
		self.valuesArray.append(thisValue) 
	def setAttributes():
		pass
		
	
	
		
def openFileAndRead():
	with open('realWeatherData.csv', 'rb') as myfile:
		myreader = csv.reader(myfile, delimiter= ' ', quotechar = '|')
		count = 0
		thisString = ""
		for row in myreader:
			thisString += ''.join(row)
			count += 1
			#print ''.join(row)
			if(count % 1 == 0):
				rowObject = DataPoint(thisString)
				rowObject.makeArray()
				strings.append(thisString)
				rowObjects.append(rowObject)
				thisString = ""			

def getGoodDataPoints():
	counter = 0
	for i in range(0, len(rowObjects) -1):
		if (rowObjects[i].valuesArray[6] != '' and rowObjects[i].valuesArray[6] != '9999' and rowObjects[i].valuesArray[6] != '-9999'):
			if(rowObjects[i].valuesArray[11] != '' and rowObjects[i].valuesArray[11] != '9999' and rowObjects[i].valuesArray[11] != '-9999'):
				counter+=1
				goodDataArray.append(rowObjects[i])
	return counter

def getRowObjects():
	return rowObjects
def getStrings():
	return strings
