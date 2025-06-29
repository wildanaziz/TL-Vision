import wandb
from ultralytics import YOLO
from wandb.integration.ultralytics import add_wandb_callback
import os
from roboflow import Roboflow
    
model= YOLO ("yolov8n.pt")


wandb.init(
    project="training",
    name="yolo-vision-run",
    config={
        "epochs": 10,
        "imgsz":640,
    }
)
data_path = r"F:\FILKOM\robotiik\TL-Vison2\samuel-lw5-2\data.yaml"

if not os.path.exists(data_path):
    print(f"Data path {data_path}")
    wandb.finish()
    exit()

add_wandb_callback(model)

try:
    model.train(
        project ="vision-training",
        data=data_path,
        epochs=10,
        imgsz=640,
    )
    best_model_path = os.path.join("runs", "detect", "train", "weights", "best.pt")

    model.val()

except Exception as e:
    print(f"training Failed :{e}")

finally:
    wandb.finish()
    print(f"wandb session finished")