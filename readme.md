<p align="center">
  <img src="https://img.shields.io/badge/ICME2025-Accepted-brightgreen?style=for-the-badge&logo=ICME" alt="ICME2025 Accepted"/>
</p>

<p align="center">
  <h1 align="center">HMPNet：A Feature Aggregation Architecture for Maritime Object Detection from a Shipborne Perspective</h1>
  <h2 align="center">🎉 Accepted at ICME2025! 🎉</h2>
  <h3 align="center"><a href="URL">View Paper</a></h3>
</p>

<p align="center">
  <img src="https://github.com/xi029/HMPNet/blob/master/img/images.png" alt="HMPNet Overview" width="70%"/>
</p>

---

## 🚀 Introduction

We are thrilled to announce that our paper **HMPNet: A Feature Aggregation Architecture for Maritime Object Detection from a Shipborne Perspective** has been accepted for presentation at **ICME2025**! This marks a significant milestone in our journey, reflecting countless hours of research, development, and unwavering perseverance.

> **"Hard work and dedication always pay off."**

---

## 🔧 How to Use

Follow the instructions below to set up and experiment with HMPNet.

---

## 🖥️ Environment

- **GPU:** NVIDIA RTX 4090
- **Python:** 3.10
- **PyTorch:** 2.0.2

---

## 📚 Table of Contents

- [⚙️ Installation](#-installation)
- [📦 Dataset Preparation](#-dataset-preparation)
- [🚀 Training & Evaluation](#-training--evaluation)
- [📄 Citation](#-citation)
- [🤝 Acknowledgement](#-acknowledgement)
- [📜 License](#-license)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/HMPNet.git
cd HMPNet
```

### 2. Create and Activate a Python Virtual Environment

```bash
conda create -n HMPNet python=3.10
conda activate HMPNet
```

### 3. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

---

## 📁 Dataset Preparation

1. **Download the maritime object detection dataset** (or use your own dataset).
2. **Organize the dataset in YOLO format:**

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

3. **Update the dataset path** in the configuration file (e.g., `data.yaml`).

---

## 🎓 Training and Evaluation

### Training from Scratch

```bash
python train.py
```

### Validation

```bash
python val.py
```

### Testing

```bash
python val.py split='test'
```

---

## 🌟 Acknowledgements

We sincerely thank the following projects for their inspiring and foundational contributions:

- [ultralytics](https://github.com/ultralytics/ultralytics)
- [PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection)
- [ParameterNet](https://parameternet.github.io/)
- [DEA-Net](https://github.com/cecret3350/DEA-Net)
- [RTDETR](https://zhao-yian.github.io/RTDETR/)

Your wonderful code and insights have greatly influenced our work.

---

## 📝 Citation

If you find this repository useful, please consider citing our paper:

```bibtex
@article{yourpaper2025,
  title={HMPNet: A Feature Aggregation Architecture for Maritime Object Detection},
  author={Your Name and Collaborators},
  journal={ICME2025 Proceedings},
  year={2025}
}
```

---

## 📜 License

This project is licensed under the **GPL-3.0 License**. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <img src="https://img.shields.io/badge/Research-Forward-blue?style=for-the-badge&logo=researchgate" alt="Research Forward"/>
  <br>
  <em>Committed to advancing maritime object detection research one step at a time.</em>
</p>
