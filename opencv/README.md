# OpenCV

Apa itu OpenCV? OpenCV merupakan sebuah library yang bisa kita gunakan untuk melakukan pengolahan gambar, video, atau **pengolahan dari kamera secara realtime**. OpenCV bersifat open-source, dan bisa digunakan untuk mengolah citra yang dikonversi dari analog ke digital sehingga kita bisa melakukan operasi-operasi pengolahan citra. Pemrosesan gambar bisa membantu kita untuk melakukan perbaikan kualitas gambar, menghilangkan noise, identifikasi gambar, deteksi warna, dan lain-lain.

## Instalasi


### Windows
1. Download dan Install Anaconda
Kamu dapat mengunjungi website [anaconda](www.anaconda.com/products/individual#Downloads)
2. Pilih versi 64-bit
3. Ikuti proses instalasi dan pastikan checklist "Add Anaconda3 to my PATH environment variable"
4. Membuat environtment baru
```bash
conda create --name opencv-env
```
5. mengaktifkan environment
```bash
conda activate opencv-env
```
6. install opencv pada environment yang telah dibuat
```bash
conda install -c conda-forge opencv
```
7. Periksa Instalasi opencv
```python
import cv2 as cv
cv.__version__
```


### Ubuntu (Linux)
**Python**

Untuk OpenCV versi python bisa langsung diinstall memakai package manager apt, seperti berikut:

```bash
sudo apt install python3-opencv -y
```

**C++**

Untuk OpenCV C++ bisa memakai library ataupun install dari source. Untuk memudahkan kita hanya akan cover bagian library.

```bash
sudo apt install libopencv-dev -y
```

## Konsep

### Dasar OpenCV

**Read, Display, Write Image**

Read - Pembacaan suatu gambar dilakukan dengan fungsi imread().

```c++
imread(filename, flags)
```

- filename: berisi path ke file gambar
- flags: opsional, berisi argumen-argumen yang membuat pemrosesan gambar lebih spesifik

Display - Jika ingin menampilkan suatu gambar, bisa dilakukan dengan fungsi imshow().

```c++
imshow(windowname, image)
```

- windowname: berisi nama window yang akan ditampilkan
- image: berisi path ke variabel (Mat) gambar

Write - Penulisan suatu gambar dilakukan dengan fungsi imread().

```c++
imwrite(filename, image)
```

- filename: berisi path untuk melakukan save
- image: berisi path ke variabel (Mat) gambar

**Penggunaan**

Berikut adalah penggunaan sederhana dari OpenCV yang menggunakan fungsi-fungsi diatas.

```c++
// library
#include<opencv2/opencv.hpp>
#include<iostream>

// namespaces
using namespace std;
using namespace cv;

Mat img_grayscale = imread("test.jpg", 0); // read
imshow("grayscale image", img_grayscale); // display

waitKey(0); // wait for a keystroke
destroyAllWindows(); // Destroys all the windows created

imwrite("grayscale.jpg", img_grayscale); // write
```

### Video di OpenCV

Kita bisa memakai VideoCapture() untuk melakukan pengambilan frame dari video/camera.

```c++
cap = cv::VideoCapture(0);
while (cap.isOpened()) {
	cv::Mat frame;

	if (!cap.read(frame))
		break;
	cv::imshow("frame", frame);

  if (cv::waitKey(30) == 'q')
    break;
}
```

### Color Spaces

**BGR**

<div align="center">
<img alt="RGB Color Space" src="https://docs.opencv.org/3.4/Threshold_inRange_RGB_colorspace.jpg" />
</div>

Format BGR merupakan format default yang digunakan oleh OpenCV untuk membaca dan menulis gambar. Color space ini memiliki elemen:
1. Blue
2. Green
3. Red

**RGB**

Sama dengan BGR. Bedanya, posisi _channel_ B dan R ditukar. Format ini merupakan format yang banyak perangkat gunakan untuk membaca dan mengeluarkan gambar. Color space ini memiliki elemen:
1. Red
2. Green
3. Blue

**HSV**

<div align="center">
<div style="background-color: white; max-width: 24em;">
<img alt="HSV Color Space" src="https://buzzneers.com/wp-content/uploads/2020/08/HSV_color_solid_cylinder-2048x1536.png" />
</div>
</div>

Berbeda dengan Color space lainnya, HSV hanya menggunakan satu _channel_ (Hue) untuk mendeskripsikan warna dan channel lainnya menggunakan warna. Biasanya color space ini berguna untuk menentukan warna tanpa dipengaruhi oleh cahaya.

**Grayscale**

<div align="center">
<img alt="Grayscale Color Space" src="https://i0.wp.com/theailearner.com/wp-content/uploads/2018/10/Capture.png?resize=539%2C238&ssl=1" />
</div>

Grayscale memperhitungkan semua aspek gambar dalam satu channel. Biasanya color space ini digunakan apabila tujuan pemrosesan gambar tidak memperhitungkan warna.

Untuk melakukan perubahan dalam color space sebuah gambar di OpenCV, dapat dilakukan melalui:

```c++
cvtColor(inputFile, outputFile, colorSpace)
```

### Color Detection

Dalam melakukan deteksi warna di image, biasanya color space yang digunakan yaitu HSV. Berikut adalah contoh program untuk deteksi warna sekita hue 150: 

```c++
Mat framehsv; 
cvtColor(frame, framehsv, COLOR_BGR2HSV); 

int hue = 150;
int thresh = 40;

Scalar minHSV = cv::Scalar(hue - thresh, hue - thresh, hue - thresh)
Scalar maxHSV = cv::Scalar(hue + thresh, hue + thresh, hue + thresh)

Mat maskHSV, resultHSV;
inRange(brightHSV, minHSV, maxHSV, maskHSV);
bitwise_and(brightHSV, brightHSV, resultHSV, maskHSV);

imshow("Result HSV", resultHSV)
```

## Compile Code

C++

```
g++ <file> -o main `pkg-config --cflags --libs opencv4`
```

### Operasi Basic

https://docs.opencv.org/3.4/d3/df2/tutorial_py_basic_ops.html

### Operasi Aritmetik

https://docs.opencv.org/3.4/d0/d86/tutorial_py_image_arithmetics.html