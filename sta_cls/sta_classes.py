import os
import cv2
import shutil
import xml.etree.ElementTree as ET
import traceback
import argparse


parser = argparse.ArgumentParser(description='Simple training script for training a RetinaNet network.')
parser.add_argument('--voc-path', default='./configs/mouse.yml', help='project file')
args = parser.parse_args()


def parse_xml(fname):
    xml_anno = ET.parse(fname)

    obj = xml_anno.find('size')
    width = float(obj.find('width').text)
    height = float(obj.find('height').text)

    for obj in xml_anno.findall('object'):
        #class_name = obj.find('name').text.lower().strip()
        class_name = obj.find('name').text.strip()
        return class_name


if __name__ == '__main__':
    clses = set()
    xml = os.path.join(args.voc_path, 'Annotations')
    for f in os.listdir(xml):
        try:
            clses.add(parse_xml(os.path.join(xml, f)))
        except:
            traceback.print_exc()
    print(clses)
    print('Total classes is:{}'.format(len(clses)))
