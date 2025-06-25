import imageio.v2 as imageio
import glob
import os

def create_gif(folder, output_name):
    files = sorted(glob.glob(os.path.join(folder, "*.jpg")))
    if not files:
        print(f" Tidak ada file .jpg ditemukan di folder: {folder}")
        return
    frames = [imageio.imread(file) for file in files]
    imageio.mimsave(output_name, frames, duration=0.5)
    print(f"GIF berhasil dibuat: {output_name}")

create_gif(r"D:\TL-Vision\weeks\week-6\subs\ezra\runs\detect\pred_yolov5_before", "yolov5_before.gif")
create_gif(r"D:\TL-Vision\weeks\week-6\subs\ezra\runs\detect\pred_yolov5_after", "yolov5_after.gif")
create_gif(r"D:\TL-Vision\weeks\week-6\subs\ezra\runs\detect\pred_yolov8_before", "yolov8_before.gif")
create_gif(r"D:\TL-Vision\weeks\week-6\subs\ezra\runs\detect\pred_yolov8_after", "yolov8_after.gif")
