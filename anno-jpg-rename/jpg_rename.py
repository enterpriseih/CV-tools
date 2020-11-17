import os
import argparse
import time

parser = argparse.ArgumentParser(description='Simple training script for training a RetinaNet network.')
parser.add_argument('--jpg-path', default='./configs/mouse.yml', help='project file')
args = parser.parse_args()


def file_rename():
    pass

if __name__ == '__main__':
    for fname in os.listdir(args.jpg_path):

        new_name_prefix = str(time.time()).replace('.', '')

        #print(new_name_prefix)
        os.rename(os.path.join(args.jpg_path, fname), os.path.join(args.jpg_path, new_name_prefix + '.jpg'))
