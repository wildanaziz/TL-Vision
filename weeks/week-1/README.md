# 🚀 **Week 1: Bonding Session and Introduction to Vision Amarine**  

## 🎯 **Tujuan Pembelajaran**  
Pada minggu pertama ini, kita akan berfokus pada pemahaman dasar tentang **Vision Amarine**, mengenal tools dan framework yang akan digunakan sepanjang roadmap ini, serta memahami konsep dasar dalam pengembangan aplikasi Computer Vision.  

---

## 📝 **Materi Pembelajaran**  

### ✅ **1. Pemaparan Roadmap Pembelajaran Vision Amarine**  
Pada sesi ini, kita akan membahas **roadmap pembelajaran** yang akan ditempuh, termasuk:  
✔️ Gambaran besar topik yang akan dipelajari setiap minggu  
✔️ Tools dan framework yang akan digunakan dalam pengembangan Computer Vision  
✔️ Studi kasus yang akan dikerjakan dalam bentuk **mini-project dan final project**  

---

### ✅ **2. Pengenalan Tools dan Framework Vision Amarine**  
Dalam pengembangan aplikasi Computer Vision, kita akan menggunakan berbagai **tools dan framework** berikut:  

| 🔧 Tools / Framework  | 📌 Kegunaan  |
|----------------------|----------------------------------|
| Python | Bahasa pemrograman utama untuk Computer Vision |
| OpenCV | Library untuk pemrosesan gambar dan video |
| TensorFlow/Keras | Framework untuk deep learning dan model AI |
| YOLO (You Only Look Once) | Model untuk object detection secara real-time |
| Roboflow | Platform untuk pengelolaan dataset dan labeling |
| Streamlit | Framework untuk membangun aplikasi web berbasis AI |
| ROS 2 | Framework untuk integrasi Computer Vision dalam robotika |
| Jetson Orin | Edge device untuk AI deployment |

📌 **Aksi**:  
- Pastikan kamu telah menginstal **Python** dan mengenal **Jupyter Notebook / VS Code / PyCharm**  
- Pahami kegunaan masing-masing tools di atas  

---

### ✅ **3. Pengenalan Konsep Dasar dari Tools dan Framework yang Digunakan**  
Sebelum masuk ke implementasi, kita akan membahas **konsep dasar** yang mendasari tools dan framework yang akan digunakan:  

✔️ **Image Processing**: Cara kerja manipulasi gambar menggunakan OpenCV  
✔️ **Deep Learning untuk Computer Vision**: Dasar-dasar CNN dan bagaimana AI mengenali objek dalam gambar  
✔️ **Object Detection vs Image Classification**: Perbedaan dalam penerapan Vision AI  
✔️ **Model Training Pipeline**: Proses pelatihan model dari dataset hingga deployment  
✔️ **Edge Computing**: Implementasi model AI pada perangkat keras seperti Jetson Orin  

📌 **Aksi**:  
- Pelajari perbedaan **image classification, object detection, dan segmentation**  
- Eksplorasi **dataset** untuk pemrosesan gambar  
- Pahami workflow **training, testing, dan deployment model**  

---

## 📌 **Studi Kasus: Diskusi Kelompok**  
Kamu akan berdiskusi dalam kelompok untuk menjawab pertanyaan berikut:  

1️⃣ **Apa tantangan terbesar dalam Computer Vision saat ini?**  
2️⃣ **Bagaimana peluang Computer Vision dalam industri seperti kesehatan, otomotif, dan keamanan?**  
3️⃣ **Bagaimana model seperti YOLO bisa diterapkan dalam kehidupan sehari-hari?**  

📌 **Aksi**:  
- Diskusikan dengan kelompokmu dan rangkum hasilnya dalam sebuah presentasi singkat  

---

## 🛠️ **Side Project: Instalasi & Environmental Development Settings**  

Agar siap menghadapi tantangan dalam minggu-minggu berikutnya, kita akan melakukan **setup lingkungan pengembangan**:  

### 🔹 **1. Instalasi Python dan Virtual Environment**  
Gunakan perintah berikut untuk menginstal dan mengatur environment:  

```bash
# Instalasi Python (jika belum terinstal)
sudo apt update && sudo apt install python3 python3-pip

# Buat virtual environment
python3 -m venv vision_env
source vision_env/bin/activate  # Aktifkan environment (Linux/macOS)
vision_env\Scripts\activate  # (Windows)

# Instal dependensi dasar
pip install opencv-python numpy matplotlib tensorflow keras roboflow streamlit
```

📌 Aksi:
- Pastikan semua tools telah terinstal
- Coba jalankan kode berikut untuk menguji OpenCV:
```python
import cv2
print("OpenCV version:", cv2.__version__)
```

### 🔹 **2. Forking Week Repository dan Struktur File Direktori Proyek** 
Setiap **Vision Amarineer** dapat **fork repository utama**, mengerjakan studi kasus atau side project di dalam **fork mereka**, lalu melakukan **pull request (PR)** ke repository utama untuk pengumpulan hasil kerja mereka. Ini juga akan memberikan transparansi, memungkinkan kolaborasi yang lebih baik serta **memudahkan PIC dalam memantau progress Vision Amarineer**.

```plaintext
vision-roadmap/
│── week-1/
│   │── study-case/
│   │   │── nama-peserta-1/
│   │   │   │── readme.md   # Deskripsi studi kasus yang dikerjakan peserta
│   │   │   │── hasil-analisis.ipynb  # Notebook atau kode yang dikerjakan
│   │   │── nama-peserta-2/
│   │── side-project/
│   │   │── nama-peserta-1/
│   │   │   │── readme.md   # Dokumentasi hasil side project peserta
│   │   │   │── setup-code/  # Folder berisi kode yang dikerjakan
│── week-2/
│── ...
│── final-project/
│   │── nama-peserta-1/
│   │── nama-peserta-2/
│── README.md  # Dokumentasi utama
```

**📌 Petunjuk Forking dan Pengumpulan Hasil**

1️⃣ Fork Repository Ini

Klik tombol Fork di sudut kanan atas repository ini untuk membuat salinan di akun GitHub-mu.

2️⃣ Clone Repository ke Lokal
```bash
git clone https://github.com/username/TL-Vision.git
cd TL-Vision
```

3️⃣ Buat Branch Baru untuk Masing-Masing Week
```bash
git checkout -b week-1-username
```

4️⃣ Tambahkan Folder dengan Namamu di study-case dan side-project
```bash
mkdir week-1/study-case/username
mkdir week-1/side-project/username
```

5️⃣ Tambahkan Dokumentasi (readme.md) dalam Foldermu
```markdown
-- Contoh --
# 📌 Studi Kasus - Week 1

## 🎯 Deskripsi  
Diskusi tentang tantangan dan peluang dalam Computer Vision, serta implementasi awal image processing.

## 🚀 Implementasi  
- Instalasi OpenCV dan percobaan kode dasar.
- Eksplorasi dataset terkait Computer Vision.

## 📊 Hasil Analisis  
Tambahkan ringkasan atau hasil analisismu di sini.
```

7️⃣ Buat Pull Request (PR) ke Repository Utama
- Buka repository utama (TL-Vision).
- Klik Pull Requests > New Pull Request.
- Pilih branch dari fork-mu, lalu ajukan PR.

📌 Proses Review dan Update Repo Utama

- PR akan direview oleh PIC dan jika sudah sesuai akan di-merge ke repo utama.
- Setelah di-merge, Vision Amarineer bisa melakukan git pull untuk mendapatkan update terbaru dari repo utama.
---

## 🎯 Target Akhir Week 1

✅ Memahami roadmap pembelajaran Vision Amarine  
✅ Menginstal dan menyiapkan environment pengembangan  
✅ Mengenal tools dan framework yang akan digunakan  
✅ Berpartisipasi dalam diskusi studi kasus  

🚀 Selamat belajar! Week berikutnya kita akan mulai eksplorasi [OpenCV!](/weeks/week-2/)


