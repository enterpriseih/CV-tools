import os
import argparse
from sta_cls.sta_classes import parse_xml

parser = argparse.ArgumentParser(description='Prepare voc.')
parser.add_argument('--voc', default='./voc', help='voc path')
parser.add_argument('--yolo', default='./yolo', help='yolo path')
args = parser.parse_args()


def print_cls():
    clses = set()
    anno_path = os.path.join(args.voc, 'Annotations')
    for f in os.listdir(anno_path):
        clses.add(parse_xml(os.path.join(anno_path, f)))
    print(clses)

def chk():
    pass

def main():
    print_cls()
    chk()

if __name__ == '__main__':
    main()
