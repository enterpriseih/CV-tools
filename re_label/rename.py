import os

for f in os.listdir('JPEGImages'):

    path = os.path.join('JPEGImages', f)

    os.rename(path, os.path.join('JPEGImages', f.replace('smoke_b', '')))
