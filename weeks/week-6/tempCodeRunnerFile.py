import onnxruntime as ort

providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
session = ort.InferenceSession(r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\yolov5s-result\weights\best.onnx", providers=providers)
print(session.get_providers())