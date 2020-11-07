rm -rf ./yolo/

mkdir yolo
mkdir yolo/images yolo/labels
mkdir yolo/images/train yolo/images/val
mkdir yolo/labels/train yolo/labels/val
mkdir yolo/biaozhu

# 1. create txt
python xml2txt.py

# 2. pic
mkdir yolo/tupian
cp ./voc/JPEGImages/* yolo/tupian/

python del_redun.py

python move_file.py

rm -rf yolo/tupian yolo/biaozhu
