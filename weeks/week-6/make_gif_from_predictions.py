from PIL import Image
import glob
import os

def create_gif_from_folder(image_folder, output_gif, duration=500):
    # Ambil semua gambar JPG di folder
    image_files = sorted(glob.glob(os.path.join(image_folder, "*.jpg")))
    if not image_files:
        print(f"Tidak ada gambar di {image_folder}")
        return

    # Load gambar pertama
    frames = [Image.open(image_files[0])]

    # Load gambar berikutnya
    for image_file in image_files[1:]:
        frames.append(Image.open(image_file))

    # Simpan jadi gif
    frames[0].save(
        output_gif,
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        duration=duration,
        loop=0,
    )

    print(f"GIF berhasil dibuat: {output_gif}")

# Path hasil prediksi YOLOv8 sebelum dan sesudah export
pred_before = r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect\pred_yolov8_before"
pred_after  = r"C:\Users\ACER\.vscode\TL-Vision\weeks\week-6\runs\detect\pred_yolov8_after"

# Bikin GIF untuk before export
create_gif_from_folder(pred_before, "yolov8_before_export.gif")

# Bikin GIF untuk after export
create_gif_from_folder(pred_after, "yolov8_after_export.gif")
