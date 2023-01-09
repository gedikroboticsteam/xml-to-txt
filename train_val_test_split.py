import os
from pathlib import Path


def repeat(begin, finish, fileExtension):
    totalList = []
    for i in range(begin, finish, 4):
        newList = []
        r = 6 - len(str(i))
        for j in range(r):
            newList.append(str(0))
        totalList.append("frame_" + "".join(newList) + str(i) + fileExtension) # fileExtension => .jpg or .txt
    return totalList
def move(imagesOrLabels, trainOrValOrTest, trainOrValOrTestFiles):
    FOLDER_PATH = f"/home/eliftosun/Downloads/Teknofest UYZ 2021 Etiketli Veriler/{imagesOrLabels}"
    DESTINATION_PATH = f"/home/eliftosun/Downloads/Teknofest UYZ 2021 Etiketli Veriler/{trainOrValOrTest}/{imagesOrLabels}"
    os.mkdir(DESTINATION_PATH) # train, val, test icin ayri ayri
    # print(len(os.listdir(DESTINATION_PATH)))
    # print(len(os.listdir(FOLDER_PATH))*0.3) # TRAIN = 2520, VAL = 540, TEST = 540
    def repeatTrainValTest(Files):
        for fileName in Files:
            source_path = FOLDER_PATH + "/" + fileName
            destination_path = DESTINATION_PATH + "/" + fileName
            if os.path.exists(source_path):
                Path(source_path).rename(destination_path)
    repeatTrainValTest(trainOrValOrTestFiles)

trainFiles = repeat(0, 10080, ".txt")
valFiles = repeat(10080, 12240, ".txt")
testFiles = repeat(12240, 14400, ".txt")
move("labels","train",trainFiles)
move("labels","val",valFiles)
move("labels","test",testFiles)