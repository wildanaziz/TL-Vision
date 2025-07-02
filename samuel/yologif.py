import cv2
import imageio

video_path = r"F:\FILKOM\robotiik\TL-Vison2\runs\detect\predict\amarine_dataset_ember.avi"
gif_path = "hasil_prediksi.gif"

vid = cv2.VideoCapture(video_path)
frames = []

success, frame = vid.read()
while success:
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frames.append(frame_rgb)
    success, frame = vid.read()

imageio.mimsave(gif_path, frames, fps=5)
print(f"GIF berhasil dibuat: {gif_path}")
