import os, re
import xml.etree.ElementTree as ET


LABEL_FOLDER = "../train/labels" # train-val-test icin ayri ayri yolu ekleyin
# print(os.listdir(LABEL_FOLDER))
DESTINATION_SOURCE = "../train/new_labels"
dictionary = {"Taşıt":0,"İnsan":1,"UAP":2,"UAİ":3}
os.mkdir(DESTINATION_SOURCE)
regex = "[a-zA-Z0-9-_]+\."
for xmlName in os.listdir(LABEL_FOLDER):
    tree = ET.parse(LABEL_FOLDER+"/"+xmlName)
    root = tree.getroot()
    for obj in root.findall("object"):
        label_name = obj.find("name").text
        xmin = obj.find("bndbox").find("xmin").text
        ymin = obj.find("bndbox").find("ymin").text
        xmax = obj.find("bndbox").find("xmax").text
        ymax = obj.find("bndbox").find("ymax").text
        for name, label in dictionary.items():
            if name == label_name:
                label_name = label
        fileName = "".join(re.findall(regex, xmlName))
        newXmlPath = DESTINATION_SOURCE+"/"+fileName+"txt"
        with open(newXmlPath, "a") as file:
            file.write(f"{label_name}\t{xmin}\t{ymin}\t{xmax}\t{ymax}\n")

