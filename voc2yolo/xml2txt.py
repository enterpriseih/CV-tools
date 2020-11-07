import os
import cv2
import shutil
import xml.etree.ElementTree as ET
import traceback

CLASSES = ['face', 'part_face', 'bow_face', 'up_face', 'chair', 'glasses', 'side_face']
XML_DIR = './voc/Annotations/'
JPEG_DIR = './voc/JPEGImages/'
LABEL_DIR = './yolo/biaozhu'

def parse_xml(fname):
    xml_anno = ET.parse(os.path.join(XML_DIR, fname))
    annos = []

    try:
        obj = xml_anno.find('size')
        width = float(obj.find('width').text)
        height = float(obj.find('height').text)

        if width < 10 or height < 10:
            img = cv2.imread(os.path.join(JPEG_DIR, fname.replace('.xml', '.jpg')))
            height, width, channel = img.shape
    except:
        img = cv2.imread(os.path.join(JPEG_DIR, fname.replace('.xml', '.jpg')))
        height, width, channel = img.shape

    for obj in xml_anno.findall('object'):
        bndbox_anno = obj.find('bndbox')
        xmin = float(bndbox_anno.find('xmin').text)
        ymin = float(bndbox_anno.find('ymin').text)
        xmax = float(bndbox_anno.find('xmax').text)
        ymax = float(bndbox_anno.find('ymax').text)


        if xmin < 0: xmin = 0
        if ymin < 0: ymin = 0
        if xmax >width: xmax = width
        if ymax > height: ymax = height

        class_name = obj.find('name').text.lower().strip()

        annos.append((class_name, xmin, ymin, xmax, ymax, width, height))

    return annos

def gen_txt(fname, annos):
    f = open(os.path.join(LABEL_DIR, fname.replace('.xml', '.txt')), 'w')
    for anno in annos:
        try:
            class_name, xmin, ymin, xmax, ymax, width, height = anno
            cls = CLASSES.index(class_name)
            xmid = (xmin + xmax) / 2 / width
            ymid = (ymin + ymax) / 2 / height
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height

            f.write(' '.join((str(cls), '%3f'%xmid, '%3f'%ymid, '%3f'%w, '%3f'%h)) + '\n')
        except:
            print(fname)
            traceback.print_exc()
    f.close()
        
if __name__ == '__main__':
    for f in os.listdir(XML_DIR):
        try:
            annos = parse_xml(os.path.join(f))
            gen_txt(f, annos)
        except:
            traceback.print_exc()
