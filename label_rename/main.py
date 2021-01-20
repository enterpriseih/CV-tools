import sys
import os
import argparse
import traceback
import xml.etree.ElementTree as ET
import xml.dom.minidom
import cv2
import shutil


parser = argparse.ArgumentParser(description='Simple training script for training a RetinaNet network.')
parser.add_argument('--inputs', default='/home/work/datasets/VOC/voc', help='')
parser.add_argument('--outputs', default='/home/work/yangfg/tmp', help='')
args = parser.parse_args()


DST_CLS = {'car': 'car', 'bus': 'car'}


def label_rename(input_xml, output_xml):
    tree = ET.parse(input_xml)

    root = tree.getroot()

    for child in root:
        if child.tag == 'object':
            for sub in child:
                if sub.tag == 'name':
                    sub.text = DST_CLS[sub.text]

    tree.write(output_xml)

    return


if __name__ == '__main__':
    os.makedirs(args.outputs, exist_ok=True)

    for f in os.listdir(args.inputs):
        try:
            label_rename(os.path.join(args.inputs, f), os.path.join(args.outputs, f))
        except:
            traceback.print_exc()
