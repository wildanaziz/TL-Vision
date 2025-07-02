# from roboflow import Roboflow
# rf = Roboflow(api_key="rmhZPWg6EXbjWphEJc4j")
# project = rf.workspace("visionamarine").project("turtle-ymyld")
# version = project.version(1)
# dataset = version.download("yolov5")

# import torch
# print(torch.cuda.is_available())
# print(torch.cuda.get_device_properties(0))

# from roboflow import Roboflow
# rf = Roboflow(api_key="rmhZPWg6EXbjWphEJc4j")
# project = rf.workspace("visionamarine").project("turtle-ymyld")
# version = project.version(1)
# dataset = version.download("yolov8")
# print(dataset.location)

# from ultralytics import YOLO
# print(YOLO('yolov8n.pt').device)

# import onnxruntime as ort

# providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
# session = ort.InferenceSession(r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\yolov5s-result\weights\best.onnx", providers=providers)
# print(session.get_providers())

providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
session = ort.InferenceSession("model.onnx", providers=providers)


