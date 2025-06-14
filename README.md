
# Crater and Boulder Detection with YOLOv8 🚀

This repository contains our implementation for detecting lunar craters and boulders using a customized YOLOv8n model. It includes model training, inference scripts, and a simple UI for demonstration.

## Team

**Team Name:** Selene Sighters  
**Team Members:**
- Anjali Kumari (Lead)
- Tangirala Dhanunjaya Rao
- Nikunj Khandelwal

## Project Structure

```
crater-boulder-detector/
├── .gitignore
├── README.md
├── inference/
│   └── predict.py       # Inference script to test on images or videos
├── requirements.txt     # Python dependencies
├── training/
│   └── train.py         # YOLO training script using Ultralytics
└── ui/
    └── app.py           # Streamlit-based web UI for demo
```

## Dataset

- Total training images: **13,955**
- Total validation images: **3,740**
- Each image is associated with label files in YOLO format (bounding boxes).

## Training Details

We trained a YOLOv8n model using the Ultralytics `yolo` Python API. The training was done on Google Colab with a Tesla T4 GPU.

### Configuration

- **Epochs:** 15  
- **Batch Size:** 16  
- **Image Size:** 416x416  
- **Model:** yolov8n  
- **Data Augmentation:** Mosaic, CLAHE, Blur, MedianBlur, ToGray

### 🔁 Full Training Logs

| Epoch | Box Loss | Cls Loss | DFL Loss | Instances | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|-------|----------|----------|----------|-----------|-----------|--------|---------|---------------|
| 1     | 1.919    | 1.459    | 1.041    | 530       | 0.62      | 0.59   | 0.61    | 0.35          |
| 2     | 1.484    | 1.037    | 0.933    | 503       | 0.66      | 0.62   | 0.67    | 0.42          |
| 3     | 1.395    | 0.985    | 0.916    | 221       | 0.62      | 0.63   | 0.64    | 0.40          |
| 4     | 1.343    | 0.945    | 0.907    | 279       | 0.71      | 0.65   | 0.73    | 0.47          |
| 5     | 1.303    | 0.922    | 0.901    | 337       | 0.63      | 0.64   | 0.66    | 0.42          |
| 6     | 1.233    | 0.892    | 0.893    | 308       | 0.68      | 0.65   | 0.71    | 0.46          |
| 7     | 1.199    | 0.858    | 0.887    | 145       | 0.71      | 0.66   | 0.73    | 0.48          |
| 8     | 1.176    | 0.840    | 0.883    | 403       | 0.71      | 0.67   | 0.74    | 0.49          |
| 9     | 1.151    | 0.820    | 0.878    | 261       | 0.76      | 0.69   | 0.78    | 0.53          |
| 10    | 1.135    | 0.802    | 0.877    | 233       | 0.76      | 0.69   | 0.78    | 0.53          |
| 11    | 1.124    | 0.792    | 0.875    | 374       | 0.77      | 0.69   | 0.79    | 0.54          |
| 12    | 1.108    | 0.778    | 0.872    | 293       | 0.78      | 0.70   | 0.80    | 0.55          |
| 13    | 1.098    | 0.769    | 0.870    | 220       | 0.78      | 0.70   | 0.80    | 0.55          |
| 14    | 1.086    | 0.758    | 0.868    | 100       | 0.78      | 0.71   | 0.80    | 0.56          |
| 15    | 1.069    | 0.745    | 0.866    | 106       | 0.78      | 0.71   | 0.80    | 0.55          |

---

Final weights saved at `runs/detect/crater_boulder_fast_train2/weights/best.pt`.

---

## ✅ Final Evaluation Metrics

- **Precision:** 78.3%  
- **Recall:** 70.7%  
- **mAP@0.5:** 80.3%  
- **mAP@0.5:0.95:** 55.5%  
- **Training Time:** ~1.08 hours

---
## 🎯 Design Decisions

| Aspect                | Decision                                                                 |
|-----------------------|--------------------------------------------------------------------------|
| Model Choice          | YOLOv8n (Nano) for speed and accuracy tradeoff                           |
| Input Size            | 416x416 for sufficient detail + low compute requirements                 |
| Batch Size            | 16, optimal for T4 GPU                                                   |
| Epochs                | 15, chosen for a balanced train time and early convergence               |
| Augmentations         | Applied conservatively (probability 0.01) to avoid image degradation     |
| CLAHE, Blurs, Gray    | Improved contrast/lighting handling in various lunar surface textures    |
| Hardware              | Google Colab with Tesla T4 GPU                                           |
| Dataset Annotation    | Manual bounding boxes in YOLO format                                     |
| UI Implementation     | A basic Streamlit interface for uploading and viewing results            |

---
## Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/crater-boulder-detector.git
cd crater-boulder-detector
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```
### 3. Download the Dataset

Before training or inference, download the dataset from Google Drive:

📂 [Click here to download the dataset](https://drive.google.com/drive/folders/1MYrhCtq5oQPsNDDOUdGTkW_H1VF8yXzw?usp=drive_link)


### 4. Run Training

```bash
cd training
yolo detect train data=data.yaml model=yolov8n.pt imgsz=416 epochs=15 batch=16 workers=8 name=crater_boulder_fast_train
```

### 5. Run Inference

```bash
cd inference
python predict.py --weights ../runs/detect/crater_boulder_fast_train/weights/best.pt --source /path/to/image.jpg
```

### 6. Run UI (Optional)

```bash
cd ui
streamlit run app.py
```

# 🌕 Thank you for exploring our lunar detection project!
**End of README**
