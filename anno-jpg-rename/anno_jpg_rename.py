import os
import argparse
import time

parser = argparse.ArgumentParser(description='Simple training script for training a RetinaNet network.')
parser.add_argument('--voc-path', default='./configs/mouse.yml', help='project file')
args = parser.parse_args()


def file_rename():
    pass

if __name__ == '__main__':
    xml_path = os.path.join(args.voc_path, 'Annotations')
    jpg_path = os.path.join(args.voc_path, 'JPEGImages')
    for fname in os.listdir(xml_path):

        new_name_prefix = str(time.time()).replace('.', '')

        os.rename(os.path.join(xml_path, fname), os.path.join(xml_path, new_name_prefix + '.xml'))
        os.rename(os.path.join(jpg_path, fname.replace('.xml', '.jpg')), os.path.join(jpg_path, new_name_prefix + '.jpg'))