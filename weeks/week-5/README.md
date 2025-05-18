# Week 5: Roboflow, Introduction to YOLO & CUDA Installation

Pada minggu ke-5, kita akan mengulas **Roboflow** yang telah diajarkan oleh **Core Team**, menerapkan [reqiurements](#requirements) bagi yang belum melakukannya, serta melakukan pengenalan dan praktik langsung (*hands-on*) menggunakan **YOLO** 🤗.

## Daftar Isi
1. [Requirements](#requirements)
    - [CPU](#requirements-cpu)
    - [GPU dengan CUDA](#requirements-gpu)
2. [Installation](#installation)
    - [CPU](#cpu)
    - [GPU with CUDA](#gpu-dengan-cuda--nvidia-only)
3. [Roboflow](#roboflow)
    - [Quickstart](#quickstart)
4. [Introduction to YOLO](#yolo-dasar)
    - [Mode](#mode)

## Requirements
<a id="requirements"></a>

Nahhh, ini adalah beberapa requirements perangkat lunak dan perangkat keras untuk menjalankan YOLO, baik untuk CPU maupun GPU dengan CUDA.

### CPU
<a id="requirements-cpu"></a>

```bash
# Persyaratan untuk CPU
1. Python 3.10
2. Instalasi YOLO (pip install ultralytics)
```

### GPU dengan CUDA  (NVIDIA ONLY)
<a id="requirements-gpu"></a>

```bash
# Persyaratan untuk GPU dengan CUDA
1. Python 3.10
2. Instalasi YOLO (pip install ultralytics)
3. Conda environment (disarankan: conda create -n yolo_env python=3.10)
4. CUDA Toolkit versi 12.6
5. cuDNN versi 9.2.0
6. opencv-cuda-warped (opsional, untuk performa optimal)
7. opencv-contrib-python (pip install opencv-contrib-python)
8. PyTorch dengan CUDA 11.8 (pip install torch==1.13.1+cu118 torchvision==0.14.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html)
```
**Catatan:**
- Unduh CUDA Toolkit 12.6 dari NVIDIA Developer. Unduh cuDNN 9.2.0 dari NVIDIA Developer (register dulu atau kalau dah punya akun tinggal masuk). 
- Pastikan driver GPU NVIDIA temen-temen kompatibel dengan CUDA 12.6. 
- Gunakan Conda untuk mengelola dependensi agar lebih mudah: `conda activate yolo_env.`

## Installation
Pada section instalasi ini sebelum belajar dan menerapkan model YOLO pada masing-masing device teman-teman perlu adanya step yang wajib dilakukan yakni menginstalasi beberapa package yang dibutuhkan. **Gunanya buat apa bwangg??** Sudah pasti, untuk memaksimalkan penggunaan YOLO serta implementasi lebih lanjut nantinya 🤔.

PIC telah menetapkan beberapa **Requirements** dalam menjalankan YOLO baik diberbagai versi (YOLOv3, YOLOv5, YOLOv8, etc.). Dimana PIC membagi kedua section berbeda sesuai kemampuan device masing-masing berikut pembagiannya:

- **[CPU](#cpu-1)** 
- **[GPU with CUDA]()**

Sebelum melakukan proses instalasi sebaiknya jangan gegabah dulu kita cek spesifikasi device masing-masing agar tidak mubazir package dan mencoba memaksimalkan device yang digunakan. 

Contoh punya PIC (device Kentang PIC, **doakan semoga cepet ganti laptop GPU spek gahar😭**):

![Device PIC Kentang](/assets/img/device-pic.png)

Nah punya pic tertera hanya memiliki CPU doang tanpa VGA external (NVIDIA), jadi cukup instalasi package section **CPU** aja. kalau punya vision amarineers ada GPU Nvidia baru instalasi package section **GPU with CUDA** biar makin gacor buat training dan prediksi 🔥.

Setelah recheck spesifikasi device yang digunakan cusss kita langsung oprek dan hands-on bersama untuk instalasi 🤗.

### CPU
Apabila device temen-temen tidak memiliki GPU external such as NVIDIA bukan RADEON jadi package yang diinstal cukup CPU aja berikut cara detailnya:
1. Pastikan sudah instalasi **conda environment** seperti pada **[week-1](/weeks/week-1/README.md)**
2. Bikin **new environment** dengan nama bebas dan **wajib python 3.10 biar ga collision**
    ```bash
    ### buat dengan nama bebas
    conda create --name yolo-ultralytics python==3.10
    ```
3. Masuk kedalam **venv conda** yang telah dibuat sebelumnya
    ```bash
    ### buat dengan nama bebas
    conda activate yolo-ultralytics
    ```
4. Install package yang dibutuhkan
    ```bash
    ### bisa pake pip
    pip install ultralytics

    ### atau pake conda-forge
    conda install -c conda-forge ultralytics
    ```

Setelah selesai proses instalasi bisa langsung cuss ke section **[Roboflow](#roboflow)** atau **[YOLO](#yolo-dasar)** 🤗.

### GPU with CUDA
Disclaimer pada section **GPU with CUDA** ini PIC hanya menunjukkan proses instalasi menggunakan **OS Windows** untuk **OS Linux** karena kernelnya bermacam-macam bisa menyelami sendiri diberbagai komunitas dikarenakan beda kernel bisa beda package yang stable.

1. Pastikan sudah instalasi **conda environment** seperti pada **[week-1](/weeks/week-1/README.md)**
2. Bikin **new environment** dengan nama bebas dan **wajib python 3.10 biar ga collision**
    ```bash
    ### buat dengan nama bebas
    conda create --name yolo-ultralytics python==3.10
    ```
3. Masuk kedalam **venv conda** yang telah dibuat sebelumnya
    ```bash
    ### buat dengan nama bebas
    conda activate yolo-ultralytics
    ```
4. Install package yang **ultralytics (YOLO)**
    ```bash
    ### bisa pake pip
    pip install ultralytics

    ### atau pake conda-forge
    conda install -c conda-forge ultralytics
    ```
5. Download lewat tautan **[🔗CUDA TOOLKIT versi 12.6](https://developer.nvidia.com/cuda-12-6-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)**

    ![cuda-toolkit](/assets/img/CUDA%20TOOLKIT.png)

6. Download lewat tautan **🔗[cudNN 9.2.0](https://developer.nvidia.com/cudnn-9-2-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=Agnostic&cuda_version=12)**

    ![cudnn](/assets/img/cudnn.png)

7. Download lewat tautan **🔗[opencv-cudawarped a.k.a opencv-contrib-python](https://github.com/cudawarped/opencv-python-cuda-wheels/releases)**

    ![opencv-cudawarped](/assets/img/opencv-cudawarped.png)

8. Install package PyTorch CUDA 11.8 melalui command berikut:
    ```bash
    ### Pastikan vision amarineers sudah berada di environment yolo yang telah dibuat

    # CUDA 11.8
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu118
    ```

Untuk proses cara instalasi dari package yang telah di download akan disampaikan di Transfer Learning Week-5 onsite okieww 🤗. Karena tadi baru download package ajah wkwk.

Setelah selesai proses instalasi bisa langsung cuss ke section **[Roboflow](#roboflow)** atau **[YOLO](#yolo-dasar)** 🤗.

## Roboflow

Roboflow adalah platform yang membantu temen-temen membangun, melatih, dan menguji model komputer vision dengan lebih cepat dan lebih mudah. Dengan Roboflow, temen-temen dapat membuat dataset, melatih model, dan menguji model dengan lebih cepat dan lebih mudah.

### Quickstart
Berikut adalah langkah-langkah sederhana untuk memulai menggunakan Roboflow, mulai dari registrasi hingga mengekspor dataset dalam format .yaml untuk pelatihan YOLO:

1. Registrasi: 
- Kunjungi Roboflow dan klik **"Sign Up"** untuk membuat akun gratis. 
- Isi informasi seperti email dan kata sandi, atau masuk menggunakan akun Google/GitHub.
- Setelah registrasi, buat workspace baru (misalnya, `taskVisionAmarine`) dan project baru dengan tipe **"Object Detection"**.
    
2. **Cara Pemakaian:**
- Unggah gambar ke proyek temen-temen dengan drag-and-drop di dashboard Roboflow atau melalui kode Python menggunakan Roboflow API:
    ```python
    ### contoh penggunaan roboflow API
    from roboflow import Roboflow
    rf = Roboflow(api_key="YOUR_API_KEY")
    project = rf.workspace("your-workspace").project("your-project")
    project.upload("path/to/image.jpg")
    ```

- Gunakan Roboflow untuk mengelola dataset, menambahkan anotasi, dan menghasilkan versi dataset.

3. **Labeling dan Annotating:**
* Di dashboard proyek, klik "Annotate" di sidebar kiri, lalu pilih batch gambar untuk dilabeli.
* Gunakan alat Bounding Box (tekan `B` atau klik ikon kotak):
    - Klik dan seret untuk menggambar kotak di sekitar objek.
    - Pilih kelas untuk objek (misalnya, "mobil", "orang") dari popup.
* Untuk segmentasi, gunakan alat Polygon (tekan `P` atau klik ikon poligon) atau Smart Polygon untuk anotasi otomatis.
* Gunakan Label Assist (ikon tongkat sulap) untuk saran anotasi otomatis berdasarkan model yang sudah dilatih.
* Simpan anotasi dan lanjutkan ke gambar berikutnya menggunakan panah di antarmuka atau keyboard.

4. **Pembagian Data `Train/Val/Test`:**

* Setelah anotasi selesai, klik **"Generate"** di sidebar untuk membuat versi dataset.
* Tentukan pembagian data, misalnya:
    - `Train`: 70% (untuk pelatihan model).
    - `Val`: 20% (untuk validasi selama pelatihan).
    - `Test`: 10% (untuk evaluasi akhir model).
* Roboflow akan secara otomatis membagi dataset sesuai rasio yang temen-temen tentukan.
* temen-temen juga dapat menggunakan kode Python dengan pustaka `supervision` untuk membagi dataset secara manual:
    ```python
    import supervision as sv
    ds = sv.DetectionDataset.from_yolo(
        images_directory_path="dataset/images",
        annotations_directory_path="dataset/labels",
        data_yaml_path="dataset/data.yaml"
    )
    train_ds, test_ds = ds.split(split_ratio=0.7, random_state=42)
    val_ds, test_ds = test_ds.split(split_ratio=0.67, random_state=42)
    ```

5. **Export ke Format `.yaml` untuk YOLO:**

* Setelah dataset dihasilkan, klik **"Download"** di halaman versi dataset.
* Pilih format **YOLOv8** (atau versi YOLO lain yang kompatibel).
* Pilih opsi **"Show Download Code"** untuk mendapatkan kode Python atau langsung unduh file zip.
* Dataset yang diekspor akan berisi:
    - Folder `train`, `val`, dan `test` dengan subfolder images dan labels.
    - File `data.yaml` yang berisi konfigurasi seperti berikut:
    ```yaml
    train: ../train/images
    val: ../valid/images
    test: ../test/images
    nc: 2
    names: ['kelas1', 'kelas2']
    ```
* Gunakan file `data.yaml` ini untuk pelatihan YOLO (lihat bagian YOLO di bawah).

***Catatan:** Pastikan anotasi dalam format YOLO (satu file `.txt` per gambar, dengan format `class_index x_center y_center width height` dalam koordinat ternormalisasi). Roboflow secara otomatis menghasilkan anotasi dalam format ini saat ekspor.*


## YOLO Dasar

YOLO (You Only Look Once) adalah sebuah model komputer vision yang dikembangkan oleh Joseph Redmon dan Ali Farhadi. YOLO adalah model deteksi objek yang dapat mendeteksi objek dalam gambar dalam waktu yang relatif singkat.

### Mode

YOLO memiliki beberapa mode yang dapat digunakan untuk melatih dan menguji model. Berikut adalah beberapa mode yang tersedia:

Untuk memulai menggunakan YOLO, temen-temen dapat mengikuti step by step yang menggunakan **quick navigation** berikut:
> [Train](#train)  

> [Validation](#validation-val)  

> [Predict](#predict)

#### Train

Mode train digunakan untuk melatih model YOLO. Dalam mode ini, temen-temen dapat menggunakan dataset yang telah dibuat untuk melatih model.

1. **Persiapkan Dataset**: Pastikan temen-temen memiliki dataset dalam format yang kompatibel dengan YOLO (misalnya, format YOLO txt). temen-temen dapat menggunakan Roboflow untuk menyiapkan dataset.
2. **Instal YOLO**: Instal pustaka Ultralytics menggunakan pip:
   ```bash
   pip install ultralytics
   ```
3. **Jalankan Pelatihan:** Gunakan perintah berikut untuk melatih model YOLOv8 pada dataset temen-temen:
    ```bash
    yolo train model=yolov8n.pt data=dataset.yaml epochs=100 imgsz=640
    ```
4. **Hasil:** Setelah pelatihan selesai, model terbaik akan disimpan di folder `runs/train/exp/weights/best.pt.`

***Catatan:** Pastikan file dataset.yaml sudah dikonfigurasi dengan benar. Contoh isi dataset.yaml:*

```yaml
train: /path/to/train/images
val: /path/to/val/images
nc: 2  # jumlah kelas
names: ['kelas1', 'kelas2']  # nama kelas
```

#### Validation (Val)

Mode val digunakan untuk menguji model YOLO. Dalam mode ini, temen-temen dapat menggunakan dataset yang telah dibuat untuk menguji model. Berikut cara detailnya:

1. **Siapkan Model dan Dataset:** Pastikan temen-temen memiliki model yang telah dilatih (misalnya, best.pt) dan dataset validasi.
2. **Jalankan Validasi:** Gunakan perintah berikut untuk mengevaluasi model:
    ```bash
    yolo val model=runs/train/exp/weights/best.pt data=dataset.yaml
    ```
    * `model`: Path ke file model yang telah dilatih.
    * `data`: File konfigurasi dataset yang sama seperti saat pelatihan.
3. **Hasil:** Hasil validasi seperti metrik presisi, recall, dan mAP akan ditampilkan di terminal dan disimpan di folder `runs/val/`.

***Catatan:** Mode ini membantu temen-temen memahami seberapa baik model bekerja pada data yang tidak digunakan selama pelatihan.*

#### Predict

Mode predict digunakan untuk memprediksi objek dalam gambar menggunakan model YOLO yang telah dilatih. Dalam mode ini, temen-temen dapat menggunakan gambar yang belum pernah dilihat sebelumnya untuk memprediksi objek. Berikut cara detailnya:

1. **Siapkan Model dan Input:** Pastikan temen-temen memiliki model terlatih dan file gambar/video untuk diprediksi.
2. **Jalankan Prediksi:** Gunakan perintah berikut untuk memprediksi objek:
    ```bash
    yolo predict model=runs/train/exp/weights/best.pt source=/path/to/image.jpg
    ```
    * `model`: Path ke file model terlatih.
    * `source`: Path ke gambar, video, atau folder berisi gambar (bisa juga URL atau webcam dengan `source=0`).
3. **Hasil:** Hasil prediksi akan disimpan di folder `runs/predict/`, termasuk gambar dengan kotak deteksi (bounding boxes) dan label.
4. **Contoh Prediksi pada Video:**
    ```bash
    yolo predict model=runs/train/exp/weights/best.pt source=/path/to/video.mp4
    ```
***Catatan:** Temen-temen dapat menambahkan parameter seperti conf=0.5 untuk mengatur ambang batas kepercayaan (confidence threshold) agar hasil lebih akurat.*

## Reference
[1] Roboflow. (n.d.). *Get started with Roboflow*. Retrieved May 18, 2025, from https://roboflow.com/  
[2] Roboflow. (n.d.). *Annotate images with Roboflow*. Retrieved May 18, 2025, from https://docs.roboflow.com/annotate  
[3] Roboflow. (n.d.). *Manage datasets with Roboflow*. Retrieved May 18, 2025, from https://docs.roboflow.com/dataset  
[4] Roboflow. (n.d.). *Export datasets from Roboflow*. Retrieved May 18, 2025, from https://docs.roboflow.com/export  
[5] Ultralytics. (n.d.). Train mode. Retrieved May 18, 2025, from https://docs.ultralytics.com/modes/train/  
[6] Ultralytics. (n.d.). Validation mode. Retrieved May 18, 2025, from https://docs.ultralytics.com/modes/val/  
[7] Ultralytics. (n.d.). Predict mode. Retrieved May 18, 2025, from https://docs.ultralytics.com/modes/predict/ 



