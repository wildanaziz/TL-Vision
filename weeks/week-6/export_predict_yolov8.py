from ultralytics import YOLO
import wandb
from PIL import Image
import glob
import os

def log_predictions_to_wandb(folder, label):
    image_files = glob.glob(os.path.join(folder, "*.jpg"))
    if not image_files:
        print(f"Tidak ada gambar di {folder}")
    for img_path in image_files:
        img = Image.open(img_path)
        wandb.log({label: wandb.Image(img)})

def export_and_predict_yolov5(sample_image, use_gpu):
    print("=== Processing YOLOv5 ===")
    model_v5 = YOLO(r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\yolov5s-result\weights\best.pt")

    pred_before_dir = r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect\pred_yolov5_before"
    model_v5.predict(source=sample_image, save=True, project=r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect", name="pred_yolov5_before")
    log_predictions_to_wandb(pred_before_dir, "YOLOv5 Before Export")

    openvino_path = model_v5.export(format="openvino")

    if use_gpu:
        model_v5.export(format="engine")

    yolov5_openvino = YOLO(openvino_path)
    pred_after_dir = r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect\pred_yolov5_after"
    yolov5_openvino.predict(source=sample_image, save=True, project=r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect", name="pred_yolov5_after", imgsz=416)
    log_predictions_to_wandb(pred_after_dir, "YOLOv5 After Export")

def export_and_predict_yolov8(sample_image, use_gpu):
    print("=== Processing YOLOv8 ===")
    model_v8 = YOLO(r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\yolov8-result\weights\best.pt")

    pred_before_dir = r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect\pred_yolov8_before"
    model_v8.predict(source=sample_image, save=True, project=r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect", name="pred_yolov8_before")
    log_predictions_to_wandb(pred_before_dir, "YOLOv8 Before Export")

    openvino_path = model_v8.export(format="openvino")

    if use_gpu:
        model_v8.export(format="engine")

    yolov8_openvino = YOLO(openvino_path)
    pred_after_dir = r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect\pred_yolov8_after"
    yolov8_openvino.predict(source=sample_image, save=True, project=r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect", name="pred_yolov8_after", imgsz=416)
    log_predictions_to_wandb(pred_after_dir, "YOLOv8 After Export")

def main():
    # Cek GPU
    use_gpu = YOLO("yolov8n.pt").device.type == "cuda"

    # Path ke folder valid images yang dipakai predict
    sample_image = r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\turtle-1\valid\images"

    # Inisiasi wandb
    wandb.init(project="yolo-wandb-project", name="YOLOv5+YOLOv8-Eval", entity="syariefanwar-universitas-brawijaya")

    # Proses YOLOv5
    export_and_predict_yolov5(sample_image, use_gpu)

    # Proses YOLOv8
    export_and_predict_yolov8(sample_image, use_gpu)

    wandb.finish()

if __name__ == "__main__":
    main()
