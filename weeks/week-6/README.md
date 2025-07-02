
# 🐢 YOLOv5 vs YOLOv8 Turtle Detection

Proyek ini bertujuan membandingkan performa model YOLOv5 dan YOLOv8 dalam mendeteksi objek **turtle** menggunakan dataset khusus.

---

## 📂 Dataset

- Train images: `turtle-1/train/images`
- Validation images: `turtle-1/valid/images`
- Data config: `turtle-1/data.yaml`

### Contoh `data.yaml`:
```yaml
nc: 1
names: ['turtle']

roboflow:
  license: CC BY 4.0
  project: turtle-ymyld
  url: https://universe.roboflow.com/visionamarine/turtle-ymyld/dataset/1
  version: 1
  workspace: visionamarine
```

---

## 📦 Model & Environment

- **YOLOv5**: v7.0  
- **YOLOv8**: v8.3.78  
- Python: 3.13.2  
- Torch: 2.6.0 + CUDA 11.8  
- OpenVINO: 2025.2.0  

---

## ⚙️ Training & Export

### YOLOv5
- Training menggunakan `train.py`  
- Validasi:
  ```bash
  python val.py --weights yolov5s-result/weights/best.pt --data turtle-1/data.yaml --img 416
  ```
- Hasil mAP muncul di console dan `runs/val/exp`

### YOLOv8
- Training:
  ```bash
  yolo task=detect mode=train model=yolov8n.pt data=turtle-1/data.yaml imgsz=416
  ```
- Export ke OpenVINO:
  ```bash
  yolo export model=yolov8-result/weights/best.pt format=openvino imgsz=416
  ```
- Predict hasil OpenVINO:
  ```bash
  yolo predict model="yolov8-result/weights/best_openvino_model" source="turtle-1/valid/images" project="predict-result" name="pred_yolov8_after" imgsz=416 save=True
  ```

---

## 🧪 Validation Results

| Model   | Images | Instances | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|:------------|:---------|:-------------|:------------|:---------|:---------|:--------------|
| **YOLOv5**  | 5       | 5           | 0.0033     | 1.0     | 0.938     | 0.429         |
| **YOLOv8**  | 5       | 5           | 0.991      | 1.0     | 0.995     | 0.975         |

---

## 📊 Perbandingan Hasil Prediksi

- **YOLOv5**:
  - Saat `detect.py`, **0 detections**
  - Validasi `val.py` menghasilkan mAP bagus tapi precision rendah → indikasi threshold terlalu ketat atau model overfit

- **YOLOv8**:
  - Semua **5 images berhasil dideteksi**
  - Akurasi tinggi, precision nyaris sempurna
  - Waktu infer lebih cepat
  - Model lebih ringan dan modern

---

## 📌 Kesimpulan

- **YOLOv8 unggul di semua aspek**:
  - Precision dan mAP tinggi
  - Deteksi konsisten tanpa miss
  - Waktu inference cepat
  - Export ke OpenVINO lancar dan performa tetap stabil

**Rekomendasi:**  
Gunakan YOLOv8 untuk project turtle detection karena hasil jauh lebih stabil, akurat, dan efisien dibanding YOLOv5.

---

## 📎 Referensi

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Ultralytics Docs](https://docs.ultralytics.com/)
