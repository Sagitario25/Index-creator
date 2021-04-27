import xml.etree.cElementTree as ET

def generate (data):
	root = ET.Element ("root")
	feature = ET.SubElement (root, "feature")
	features = ET.SubElement (feature, "list")

	features.text = str ([i for i in data])

	for i in data:
		feature.append (featureXML (str (i), data [i]))

	return ET.tostring (feature, encoding = "UTF-8", method = "xml").decode ()

def featureXML (name, data):
	fRoot = ET.Element ("root")
	feature = ET.SubElement (fRoot, "feature")
	feature.set ("name", str (name))

	versionlist = ET.SubElement (feature, "versionlist")
	versionlist.text = str ([i for i in data])
	for i in data:
		version = ET.SubElement (feature, "version")
		version.set ("num", str (i))
		version.text = str (data [i])
	
	return feature