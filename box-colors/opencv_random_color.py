import random

def get_all_colors(classes, seed=2):
    class_colors = {}
    random.seed(seed)
    for cls in classes:
        class_colors[cls] = [random.randint(0, 255) for _ in range(3)]

    return  class_colors


if __name__ == '__main__':
    print(get_all_colors(['person', 'hat']))