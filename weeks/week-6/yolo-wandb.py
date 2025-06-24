import wandb
from wandb.integration.ultralytics import add_wandb_callback
from ultralytics import YOLO
import os


model = YOLO("yolov5nu.pt")  # Load a pre-trained YOLOv5 model

wandb.init(
    project="vision",  # Project name in W&B
    name="yolo-vision-run",  # Name of the run
    config={
        "epochs": 5,  # Number of epochs
        "img_size": 640,  # Image size for training
    }
)

# Path ke data.yaml
data_path = "/home/wildanaziz/AMARINE/TL-VIsion/weeks/week-6/PIC-LW-2/data.yaml"

# Periksa apakah file ada
if not os.path.exists(data_path):
    print(f"Error: File {data_path} tidak ditemukan. Silakan periksa path-nya.")
    wandb.finish()
    exit()

# Latih model
try:
    model.train(
        project="vision-training",  # Nama folder lokal berbeda dari proyek W&B
        data=data_path,
        epochs=5,
        imgsz=640
    )
    # Validasi model
    model.val()
except Exception as e:
    print(f"Training failed: {e}")
finally:
    wandb.finish()  # Selalu tutup run W&B