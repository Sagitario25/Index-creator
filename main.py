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

def printer (toPrint):
	if toPrint == "json":
		print (mng.output ())
	elif toPrint == "xml":
		import xml.dom.minidom as minidom
		xml = xmlBuilder.generate (mng.exportData ())
		print (minidom.parseString (xml).toprettyxml ())

def saver (toSave, path):
	if toSave == "json":
		mng.save (path)
	elif toSave == "xml":
		buildXML (path)

interpreter = command.Interpreter ()
interpreter.addCommand ("addFeature", mng.addFeature)
interpreter.addCommand ("addVersion", mng.addVersion)
interpreter.addCommand ("print", printer)
interpreter.addCommand ("save", saver)

if __name__ == "__main__":
	while True:
		interpreter.call (input ("---"))