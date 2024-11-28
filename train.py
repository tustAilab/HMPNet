import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('your model yaml')
    model.train(data='your yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=64,
                close_mosaic=0,
                workers=8,
                device='0', #或者cpu,
                optimizer='SGD', # using SGD
                # patience=0, # close earlystop
                # resume=True, # 断点续训
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )