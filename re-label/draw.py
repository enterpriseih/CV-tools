import os
import cv2
import json
from collections import defaultdict
import xml.etree.ElementTree as ET

BIAOZHU = './Annotations'
#BIAOZHU = './json'
OUTPUT = './output'
INPUT = './JPEGImages'
COLOR = [(0, 0, 255), (0, 255, 0)]

def parse_single_xml(xml_path):
    """处理单个voc anno文件，获得对应的标注坐标、类别标签"""
    xml_anno = ET.parse(xml_path)
    annos = []

    for obj in xml_anno.findall('object'):
        bndbox_anno = obj.find('bndbox')
        xmin = int(float(bndbox_anno.find('xmin').text))
        ymin = int(float(bndbox_anno.find('ymin').text))
        xmax = int(float(bndbox_anno.find('xmax').text))
        ymax = int(float(bndbox_anno.find('ymax').text))
        class_name = obj.find('name').text.lower().strip()
        
        annos.append((xmin, ymin, xmax, ymax, class_name))
        
    return annos

def parse_single_json(json_path):
    annos = []
    f = open(json_path)
    j = json.loads(f.read())
    for x in j.get('shapes', []):
        class_name = x.get('label', '')
        p1 = x.get('points')[0]
        xmin = int(p1[0])
        ymin = int(p1[1])
        
        p2 = x.get('points')[1]
        xmax = int(p2[0])
        ymax = int(p2[1])
        
        annos.append((xmin, ymin, xmax, ymax, class_name))

    return annos

def main():
    for x in os.listdir(BIAOZHU):
        xml_path = os.path.join(BIAOZHU, x)
        annos = parse_single_xml(xml_path)
        #annos = parse_single_json(xml_path)
        
        prefix = x[:-4]
        jpg_path = os.path.join(INPUT, prefix + '.jpg')
        im = cv2.imread(jpg_path)
        
        for anno in annos:
            text = anno[4]
            # 画矩形框
            cv2.rectangle(im, (anno[0], anno[1]), (anno[2], anno[3]), (0, 255, 0), thickness=1)
            cv2.putText(im, text, (anno[0], anno[3]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)


        cv2.imwrite(os.path.join(OUTPUT, prefix+'.jpg'), im)

if __name__ == '__main__':
    main()
