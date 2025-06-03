from ultralytics import YOLO
import ultralytics.engine.results as Results
import cv2 as cv

# cap = cv.VideoCapture("dataset/amarine_dataset_ember.mp4")

# model = YOLO("best(3).pt")  # Load a pre-trained YOLOv8 model

# model.export(format="openvino", int8=True)  # Export the model to OpenVINO format with INT8 quantization

openvino_model = YOLO("best(3)_openvino_model")

results = openvino_model("dataset/amarine_dataset_ember.mp4", show=True, device="intel:gpu")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     results = model(frame, stream=True)

#     for result in results:
#         boxes = result.boxes
#         for box in boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             class_id = int(box.cls[0])
#             class_name = model.names[class_id]
#             label = f"{class_name} {box.conf[0]:.2f}"
#             cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv.putText(frame, label, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     cv.imshow("YOLO Detection", frame)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()