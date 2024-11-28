import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':  
        model = YOLO('your  path') # 选择训练好的权重路径
        model.val(data='your yaml',
                  split='test',# split可以选择train、val、test 根据自己的数据集情况来选择.
                  imgsz=640,
                  batch=1,
                  iou=0.6, 
                  conf=0.001,
                  project='runs/val',
                  name='exp',
                  workers=8,
                  )
