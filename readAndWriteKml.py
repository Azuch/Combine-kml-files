from pykml import parser 
from lxml import etree
import sys

#Get list of ap to compare

def addToBase(file):
    with open(file) as f:
        doc = parser.parse(f).getroot()
    for fol in doc.Document.Folder:
        if fol.name == "Wifi Networks":
            print(fol.name, "***")
            listToCompare = [ap for ap in fol.Placemark]
    for apToCompare in listToCompare:
        if apToCompare.name == "":
            print(apToCompare.description)
        elif apToCompare.name not in [ap.name for ap in apList]:
            dire.append(apToCompare)

with open('base.kml') as f:
    tree = parser.parse(f)
    root = tree.getroot()

for fol in root.Document.Folder:
    if fol.name == "Wifi Networks":
        dire = fol
        apList = [ap for ap in fol.Placemark]

for i in range(1, len(sys.argv)):
    addToBase(sys.argv[i])
    print(sys.argv[i])

for ap in dire.Placemark:
    print(ap.name)
print("Till here, the code is ok")
with open("base2.kml", "wb") as f:
    tree.write(f, encoding="utf-8")
