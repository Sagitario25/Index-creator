import command
import manager
import xmlBuilder

import os

if os.path.exists ("index.json"):
	mng = manager.dataManager (open ("index.json", "r").readline ())
else:
	mng =  manager.dataManager ()
	
def export (path):
	"""Saves json"""
	print (f"{mng.output ()}\n")
	mng.save (path)

def buildXML (path):
	xml = xmlBuilder.generate (mng.exportData ())
	open (path, "w").write (xml)

interpreter = command.Interpreter ()
interpreter.addCommand ("addFeature", mng.addFeature)
interpreter.addCommand ("addVersion", mng.addVersion)
interpreter.addCommand ("output", mng.output)
interpreter.addCommand ("save", mng.save)
interpreter.addCommand ("export", export)
interpreter.addCommand ("buildXML", buildXML)

if __name__ == "__main__":
	while True:
		interpreter.call (input ("---"))