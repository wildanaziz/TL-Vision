from ultralytics import YOLO
import torch
from roboflow import Roboflow
import time  # Tambahkan modul time

start_time = time.time()  # Mulai waktu eksekusi

model = YOLO("yolov8n.pt")  # Load a pre-trained YOLOv8 model
result = model.train(data=r"D:\TL-Vision\weeks\week-6\subs\ezra\turtle-1\data.yaml", epochs=100, imgsz=640, workers=0)

end_time = time.time()  # Selesai waktu eksekusi

# Tampilkan durasi waktu
elapsed_time = end_time - start_time
print(f"\nTraining Selesai. Total waktu eksekusi: {elapsed_time:.2f} detik")
