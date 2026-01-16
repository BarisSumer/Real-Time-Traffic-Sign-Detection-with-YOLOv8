# 🚦 Real-Time Traffic Sign Detection with YOLOv8

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-purple)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-OpenCV-green)
![Accuracy](https://img.shields.io/badge/mAP50-93.2%25-brightgreen)

An autonomous driving perception system capable of detecting and classifying **34 different types of traffic signs** in real-time. This project utilizes the **YOLOv8 Small (yolov8s)** architecture trained on a comprehensive dataset.

## 🌟 Key Features
* **High Accuracy:** Achieved **93.2% mAP@0.50** on the validation set.
* **Real-Time Performance:** Optimized for fast inference using OpenCV.
* **Robust Detection:** Capable of detecting signs under various lighting conditions.

## 📊 Model Performance
The model was trained for 50 epochs.

| Metric | Value | Description |
| :--- | :--- | :--- |
| **mAP50** | **0.932** | Mean Average Precision at 0.5 IoU |
| **mAP50-95** | **0.792** | High-precision localization accuracy |
| **Precision** | **0.955** | Low false positive rate |
| **Recall** | **0.910** | High detection rate |

## 🛠️ Installation

1.  Clone the repo:
    ```bash
    git clone [https://github.com/BarisSumer/Traffic-Sign-Detection.git](https://github.com/BarisSumer/Traffic-Sign-Detection.git)
    cd Traffic-Sign-Detection
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the detection script (Webcam):
    ```bash
    python inference.py
    ```

## 🧠 Training Details
* **Framework:** Ultralytics YOLOv8
* **Model:** YOLOv8s (Small)
* **Epochs:** 50
* **Dataset:** Roboflow (Self-Driving Car Dataset)
* **Environment:** Google Colab (Tesla T4 GPU)

---
**Developer:** Barış Sümer
