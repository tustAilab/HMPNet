<p align="center">
    <h1 align="center">HMPNet：A Feature Aggregation Architecture for Maritime Object Detection from a Shipborne Perspective</h1>
     </p>
    <h3 align="center"><a href="URL">Paper</a>
    <div align="center"></div>
</p>

![image](https://github.com/xi029/HMPNet/blob/master/img/images.png)

## How to use

## Environment

- NVIDIA RTX 4090
- Python 3.10
- Pytorch 2.0.2

## Installation

**1.Clone this repository:**

```
git clone https://github.com/yourusername/HMPNet.git
cd HMPNet
```

**2.Create a Python virtual environment and activate it:**

```
conda create -n HMPNet python=3.10
conda activate HMPNet
```

**3.Install the required dependencies:**

```
pip install -r requirements.txt
```

## Dataset Preparation

**1.Download the maritime object detection dataset (or use your dataset).**

**2.Organize the dataset in YOLO format**

```
├── dataset/
    ├── train/
        ├── images/
        ├── labels/
    ├── val/
        ├── images/
        ├── labels/
    ├── test/
        ├── images/
        ├── labels/
```

**3.Update the dataset path in the configuration file (e.g., `data.yaml`).**

## Training

**To train HMPNet from scratch:**

```
python train.py
```

## validation

```
python val.py
```

## test

```
python val.py   split='test'
```

## Acknowledgement

**We sincerely thank [ultralytics](https://github.com/ultralytics/ultralytics), [PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection), [ParameterNet](https://parameternet.github.io/), [DEA-Net](https://github.com/cecret3350/DEA-Net), and [RTDETR](https://zhao-yian.github.io/RTDETR/) for providing their wonderful code to the community!**

## Citation

**If you find this repository helpful, please cite our paper:**

```
@article{yourpaper2024,
  title={HMPNet: A Feature Aggregation Architecture for Maritime Object Detection},
  author={Your Name and Collaborators},
  journal={Journal/Conference Name},
  year={2024}
}
```

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for details.
