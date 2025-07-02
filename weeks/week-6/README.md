# 📦 Week 6: YOLOv5 vs YOLOv8 + W&B Tracking

## 🎯 Tujuan
1. Benchmark performa YOLOv5 vs YOLOv8 pada deteksi **turtle**
2. Tracking training menggunakan **Weights & Biases (W&B)**

---

## 🐢 YOLOv5 vs YOLOv8 - Turtle Detection

### Dataset
- Train: `turtle-1/train/images`
- Valid: `turtle-1/valid/images`
- Config: `turtle-1/data.yaml`

### Hasil Evaluasi

| Model   | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|---------|-----------|--------|---------|--------------|
| YOLOv5  | 0.0033    | 1.0    | 0.938   | 0.429        |
| YOLOv8  | 0.991     | 1.0    | 0.995   | 0.975        |

**Kesimpulan**: YOLOv8 lebih akurat, cepat, dan konsisten. Cocok untuk deployment real-world.

---

## 📈 Tracking Model dengan W&B

### Setup
1. Daftar & login di [wandb.ai](https://wandb.ai)
2. Install:
   ```bash
   pip install wandb
   wandb login
