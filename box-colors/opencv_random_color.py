import cv2
import numpy as np

def get_all_colors(classes):
    return np.random.uniform(0, 255, size=(len(classes), 3))

if __name__ == '__main__':
    print(get_all_colors(['person', 'hat']))