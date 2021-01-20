import sys
import os
import argparse
import traceback
import xml.etree.ElementTree as ET
import xml.dom.minidom
import cv2


parser = argparse.ArgumentParser(description='Simple training script for training a RetinaNet network.')
parser.add_argument('--inputs', default='/home/work/datasets/VOC/voc', help='')
parser.add_argument('--outputs', default='/home/work/yangfg/tmp', help='')
args = parser.parse_args()


DST_CLS = ['car', 'bus']


def extract_label(input_xml, output_xml):
    tree = ET.parse(input_xml)

    root = tree.getroot()
    objs = tree.findall('object')

    for obj in objs:
        if obj.find('name').text not in DST_CLS:
            root.remove(obj)

    if 0 == len(tree.findall('object')) > 0:
        xml_str = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
        xml_str = os.linesep.join([s for s in xml_str.splitlines() if s.strip()])
        xml_str = xml_str.split('\n', maxsplit=1)[1]
        xml_str = xml_str.encode("utf-8")
        with open(output_xml, 'wb') as f:
            f.write(xml_str)

    return


if __name__ == '__main__':
    os.makedirs(os.path.join(args.outputs, 'Annotations'), exist_ok=True)
    os.makedirs(os.path.join(args.outputs, 'JPEGImages'), exist_ok=True)

    for f in os.listdir(os.path.join(args.inputs, 'Annotations')):
        try:
            extract_label(os.path.join(args.inputs, 'Annotations', f), os.path.join(args.outputs, 'Annotations', f))
        except:
            traceback.print_exc()