import os
import shutil

imgs = [x.replace('.jpg', '') for x in os.listdir('./yolo/tupian')]
lbls = [x.replace('.txt', '') for x in os.listdir('./yolo/biaozhu')]

for x in imgs:
    if x not in lbls:
        os.remove(os.path.join('./yolo/tupian', x+'.jpg'))
