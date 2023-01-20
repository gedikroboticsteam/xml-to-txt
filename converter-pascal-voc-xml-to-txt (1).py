import os, re
import xml.etree.ElementTree as ET


LABEL_FOLDER = "../Teknofest UYZ 2021 Etiketli Veriler/labels"
# print(os.listdir(LABEL_FOLDER))
DESTINATION_SOURCE = "../Teknofest UYZ 2021 Etiketli Veriler/new_labels"
dictionary = {"Taşıt":0,"İnsan":1,"UAP":2,"UAİ":3}
os.mkdir(DESTINATION_SOURCE)
regex = "[a-zA-Z0-9-_]+\."
IMAGE_FOLDER = "/home/eliftosun/Downloads/Teknofest UYZ 2021 Etiketli Veriler/images"
for xmlName in os.listdir(LABEL_FOLDER):
    tree = ET.parse(LABEL_FOLDER+"/"+xmlName)
    root = tree.getroot()
    # print(len(root.findall("object")))
    if len(root.findall("object")) > 0:
        file_name = root.find("filename").text
        print(file_name)
        w = root.find("size").find("width").text
        h = root.find("size").find("height").text
        d = 3 # size.find("depth").text
        image_size = (float(w),float(h),float(d))
        # print(f"w: {w}\th: {h}\td: {d}")
        for obj in root.findall("object"):
            label_name = obj.find("name").text
            xmin = float(obj.find("bndbox").find("xmin").text)
            ymin = float(obj.find("bndbox").find("ymin").text)
            xmax = float(obj.find("bndbox").find("xmax").text)
            ymax = float(obj.find("bndbox").find("ymax").text)
            # Transform the bbox co-ordinates as per the format required by YOLO v7
            center_x = (xmin+xmax) / 2
            center_y = (ymin+ymax) / 2
            width = (xmax- xmin)
            height = (ymax - ymin)
            # Normalise the co-ordinates by the dimensions of the image
            image_w, image_h, image_c = image_size
            center_x /= image_w
            center_y /= image_h
            width /= image_w
            height /= image_h
            for name, label in dictionary.items():
                    if name == label_name:
                        label_name = label
            fileName = "".join(re.findall(regex, xmlName))
            newXmlPath = DESTINATION_SOURCE+"/"+fileName+"txt"
            print(f"{label_name}\t{center_x}\t{center_y}\t{width}\t{height}\n")
            with open(newXmlPath, "a") as file:
                file.write(f"{label_name} {center_x} {center_y} {width} {height}\n")
    else:
        print(xmlName)
        imageName = "".join(re.findall(regex, xmlName))
        imagePath = IMAGE_FOLDER+"/"+imageName+"jpg"
        if os.path.exists(imagePath):
            os.remove(imagePath)
