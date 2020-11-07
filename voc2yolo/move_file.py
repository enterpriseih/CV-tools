import os
import sys
import argparse
import random
import shutil

def main(args):
    for f in os.listdir(args.input_images):
        seed = random.random()
        if seed < 0.1:
            shutil.move(os.path.join(args.input_images, f), os.path.join(args.output_images , 'val'))
            shutil.move(os.path.join(args.input_labels, f.replace('.jpg', '.txt')), os.path.join(args.output_labels, 'val'))
        else:
            shutil.move(os.path.join(args.input_images, f), os.path.join(args.output_images , 'train'))
            shutil.move(os.path.join(args.input_labels, f.replace('.jpg', '.txt')), os.path.join(args.output_labels, 'train'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-images', default='yolo/tupian/')
    parser.add_argument('--input-labels', default='yolo/biaozhu/')
    parser.add_argument('--output-images', default='yolo/images/')
    parser.add_argument('--output-labels', default='yolo/labels/')
    args = parser.parse_args()
    main(args)
