import os
import cv2
import shutil
import xml.etree.ElementTree as ET
import traceback

XML_DIR = './voc/Annotations/'
clses = set()

def parse_xml(fname):
    xml_anno = ET.parse(os.path.join(XML_DIR, fname))

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
        #class_name = obj.find('name').text.lower().strip()
        class_name = obj.find('name').text.strip()
        clses.add(class_name)

if __name__ == '__main__':
    for f in os.listdir(XML_DIR):
        try:
            parse_xml(os.path.join(f))
        except:
            traceback.print_exc()
    print(clses)
