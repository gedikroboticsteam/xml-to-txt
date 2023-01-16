import os, re
from pathlib import Path

IMAGES_LABELS_PATH = "/home/eliftosun/Desktop/droneImages/imagesTotal" # image+label folder(same folder)
# print(os.listdir(IMAGE_PATH))
TRAIN_PATH = "/home/eliftosun/Desktop/droneImages/train"
TEST_PATH = "/home/eliftosun/Desktop/droneImages/test"
VAL_PATH = "/home/eliftosun/Desktop/droneImages/val"
# os.mkdir(TRAIN_PATH)
# os.mkdir(VAL_PATH)
# os.mkdir(TEST_PATH)
def split(TRAIN_OR_VAL_OR_TEST_PATH, cnt):
    regex = "[a-zA-Z0-9_-]+"
    for image in os.listdir(IMAGES_LABELS_PATH):
        img = re.findall(regex, image)[0]+".jpg"
        label = "labels"+re.findall(regex,image)[0]+".txt"
        if img in os.listdir(IMAGES_LABELS_PATH) and label in os.listdir(IMAGES_LABELS_PATH):
            source_image_path = IMAGES_LABELS_PATH + "/" + re.findall(regex, image)[0] + ".jpg"
            print(source_image_path)
            destination_image_path = TRAIN_OR_VAL_OR_TEST_PATH+"/images/"+img
            source_label_path = IMAGES_LABELS_PATH + "/labels" + re.findall(regex, image)[0] + ".txt"
            print(source_label_path)
            destination_label_path = TRAIN_OR_VAL_OR_TEST_PATH + "/labels/" + label
            if os.path.exists(source_image_path):
                Path(source_image_path).rename(destination_image_path)
            if os.path.exists(source_label_path):
                Path(source_label_path).rename(destination_label_path)
            if len(os.listdir(TRAIN_OR_VAL_OR_TEST_PATH+"/images")) == cnt and len(os.listdir(TRAIN_OR_VAL_OR_TEST_PATH+"/labels")) == cnt:
                break
        else:
            print("NOT FOUND IMAGE AND LABEL")
    # print(os.listdir(IMAGES_LABELS_PATH))
# split(TRAIN_PATH, 890)
# print(1272*0.7) # 890 train
# print(1272*0.3) # 191 val, 191 test
# print(len(os.listdir(IMAGES_LABELS_PATH))/2) # => 1272