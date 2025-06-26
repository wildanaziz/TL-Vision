# Convolutional Neural Networks (CNN)

## Visualisasi

- [Demo Handwritten with CNN](https://adamharley.com/nn_vis/cnn/2d.html)  
- [CNN Explainer](https://poloclub.github.io/cnn-explainer/)

## Apa itu CNN

CNN adalah salah satu algoritma machine learning yang telah sukses
digunakan dalam berbagai aplikasi pemrosesan citra, termasuk
klasifikasi, segmentasi, dan deteksi objek. Mereka memanfaatkan lapisan
konvolusi untuk mengekstraksi fitur-fitur penting dari citra. Arsitektur
CNN dianalogikan dengan pola konektivitas otak manusia. Sama seperti
otak yang terdiri dari miliaran neuron, CNN juga memiliki neuron yang
tersusun dengan cara tertentu. Pada CNN gambar akan di representasikan
ke bentuk maatriks agar bisa di olah oleh program.

![image](/assets/img/matriks.png)

## Arsitektur CNN

CNN membagi gambar menjadi beberapa layer yaitu input layer, hidden
layer, dan output layer. Hidden layer terbagi lagi menjadi beberapa
bagian. secara garis besar hidden layer terbagi menjadi tiga yaitu
konvolusi, pooling dan fully connected.

![image](/assets/img/layer.png)

### Layer Konvolusi

Lapisan ini merupakan lapisan pertama yang digunakan untuk mengekstrak
berbagai fitur dari gambar masukan. Pada lapisan ini, operasi matematis
konvolusi dilakukan antara matriks gambar masukan dan matriks filter
dengan ukuran MxM tertentu. Dengan menggeser filter ke atas gambar
masukan, perkalian titik antara filter dan bagian gambar masukan diambil
sesuai dengan ukuran filter (MxM). Operasi ini akan dilakuakn dengan
beberapa filter sehingga menghasilkan beberapa output.  
![image](/assets/img/convolution.png)  
Outputnya disebut sebagai peta Fitur yang memberi kita informasi tentang
gambar seperti sudut dan tepinya. Nantinya, peta fitur ini diumpankan ke
lapisan lain untuk mempelajari beberapa fitur lain dari gambar masukan.

### Layer Poooling

Ouput dari covolution akan diteruskan ke Lapisan Penggabungan atau layer
pooling. Tujuan utama dari lapisan ini adalah untuk memperkecil ukuran
peta fitur yang dikonvolusi untuk mengurangi biaya komputasi. Hal ini
dilakukan dengan mengurangi koneksi antar lapisan dan beroperasi secara
independen pada setiap peta fitur. Terdapat dua jenis operasi Pooling
yaitu Max dan Min

Pada Max Pooling, elemen terbesar diambil dari peta fitur. Average
Pooling menghitung rata-rata elemen dalam bagian Gambar berukuran yang
telah ditentukan. Pooling Layer biasanya berfungsi sebagai jembatan
antara Convolutional Layer dan FC Layer.

![image](/assets/img/pooling.png)

### Layer Fully Connected (FC)

Lapisan Fully Connected (FC) adalah lapisan inti dari CNN, lapisan ini
adalah lapisan yanga mengaplikasikan algortitma neural network
konvesional. Setelah input gambar di konvolusi dan di pooling beberapa
kali, akan dihasikan beberaba matriks gambar yang ukuran piksel nya
kecil dan berisi informasi penting dari gambar input. Misalkan matriks
yang dihasilkan berjumlah 16 dan setiap matriks berukuran 5x5, maka
total piksel yang dihasilkan adalah 16x5x5 = 400 dan juga terdapat 400
angka yang merepresentasikan warna untuk setiap piksel.

Dalam lapisan ini semua nilai tersebut akan dimasukkan ke beberapa
fungsi dan setiap dari fungsi tersebut memiliki parameter-paramter yang
disebut weight. hasil dari setiap fungsi akan bernilai dari 0 hingga 1
dan nilai ini merepresentasikan tingkat keakurasian suatu fitur berada
dalam gambar.

![image](/assets/img/fitur.png)  
Misal fungsi pertama adaalah untuk mengukur tingkat keakurasian fitur
berupa adanya lingkaran dalam gambar, fungsi kedua mengukur tingkat
keakurasian fitur berupa adanya garis dengan kemiringan sekian, dan
seterusnya. weight dari setiap fungsi dan jumlah fungsi, tergantung pada
apa yang ingin di deteksi. Biasanya nilai weight pada fungsi dan jumlah
fungsi didapat dari trainning data

lapisan ini akan diulang berkali kali dari yang awalnya mengecek
fitur-fitur kecil, lalu output nilai nya dimasukan lagi ke fungsi-fungsi
untuk mendeteksi fitur-fitur yang lebih besar hilngga menghasilkan
output berupa hasil deteksi.

untuk penjelasan lebih lanjut tentang neural network silakah clik [link
ini](https://www.youtube.com/watch?v=aircAruvnKk)  
![image](/assets/img/fully.png)