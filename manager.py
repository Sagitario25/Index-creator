import json

class dataManager:
	def __init__ (self, presaved = None):
		self.features = {} #Create dict for adding all the data
		if presaved != None:
			self.features = json.loads (presaved) #Loads saved data

	def addFeature (self, featureName):
		self.features [featureName] = {} #Adds the feature to the dict

	def addVersion (self, feature, versionNumber, url):
		if not feature in self.features:
			raise Exception ("That feature doesnt exists")
		
		self.features [feature][versionNumber] = url
	
	def output (self):
		return  json.dumps (self.features)
	
	def save (self, path):
		open (path, "w").write (self.output ())

if __name__ == "__main__":
	mng = dataManager ()
	mng.addFeature ()
	print (mng.features)