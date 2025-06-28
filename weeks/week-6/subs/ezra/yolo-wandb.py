from ultralytics import YOLO
import wandb
from PIL import Image
import glob
import os

def log_predictions_to_wandb(folder, label):
    image_files = glob.glob(os.path.join(folder, "*.jpg"))
    for img_path in image_files:
        img = Image.open(img_path)
        wandb.log({label: wandb.Image(img)})

def export_and_predict_only():
    use_gpu = YOLO("yolov8n.pt").device.type == "cuda"
    sample_image = r"D:\TL-Vision\weeks\week-6\subs\ezra\turtle-1\valid\images"

    # ========== YOLOv5 ==========
    wandb.init(project="yolo-wandb-project", name="YOLOv5s-EvalOnly", entity="ezranewbie17-brawijaya-university")
    model_v5 = YOLO(r"D:\TL-Vision\weeks\week-6\subs\ezra\runs\detect\yolov5_train\weights\best.pt")

    pred_yolov5_before_dir = "runs/detect/pred_yolov5_before"
    model_v5.predict(source=sample_image, save=True, name="pred_yolov5_before")
    log_predictions_to_wandb(pred_yolov5_before_dir, "YOLOv5 Before Export")

    openvino_v5_path = model_v5.export(format="openvino")
    if use_gpu:
        model_v5.export(format="engine")

    yolov5_openvino = YOLO(openvino_v5_path)
    pred_yolov5_after_dir = "runs/detect/pred_yolov5_after"
    yolov5_openvino.predict(source=sample_image, save=True, name="pred_yolov5_after")
    log_predictions_to_wandb(pred_yolov5_after_dir, "YOLOv5 After Export")
    wandb.finish()

    # ========== YOLOv8 ==========
    wandb.init(project="yolo-wandb-project", name="YOLOv8s-EvalOnly", entity="ezranewbie17-brawijaya-university")
    model_v8 = YOLO(r"D:\TL-Vision\weeks\week-6\subs\ezra\runs\detect\yolov8_train\weights\best.pt")

    pred_yolov8_before_dir = "runs/detect/pred_yolov8_before"
    model_v8.predict(source=sample_image, save=True, name="pred_yolov8_before")
    log_predictions_to_wandb(pred_yolov8_before_dir, "YOLOv8 Before Export")

    openvino_v8_path = model_v8.export(format="openvino")
    if use_gpu:
        model_v8.export(format="engine")

    yolov8_openvino = YOLO(openvino_v8_path)
    pred_yolov8_after_dir = "runs/detect/pred_yolov8_after"
    yolov8_openvino.predict(source=sample_image, save=True, name="pred_yolov8_after")
    log_predictions_to_wandb(pred_yolov8_after_dir, "YOLOv8 After Export")
    wandb.finish()

if __name__ == '__main__':
    export_and_predict_only()
