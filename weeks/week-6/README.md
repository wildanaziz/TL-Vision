# Week 6: Deep Dive into YOLOv5 and YOLOv8 and Track ur Model Result

Pada minggu ke-6 kali ini, kita akan mengulik lebih dalam bersama-sama tentang YOLOv5 dan YOLOv8. Dimana pada week kali ini kita akan mencoba benchmarking, evaluasi model yang telah kita buat dan mencoba mencari tuning terbaik dari hasil tracking result model yang telah dilatih. So, buat para vision amarineers sebelum kita terjun bersama kita coba penuhi beberapa requirements yang dibutuhkan.

## Quick Navigation Table
1. [Requirements](#requirements)
2. [Overview](#overview)
    - [Workflow Vision](#workflow)
3. [Installation](#installation)
    - [Akses ke web wandb](#akses_ke_web_wandb)
    - [Bikin project baru](#bikin_project)
    - [Install library wandb dan setup](#install_library)
4. [Tracking ur Model YOLOv5 and YOLOv8](#tracking-ur-model-yolov5-and-yolov8)
    - [YOLOv5 dan YOLOv8](#yolov5-dan-yolov8)

## Requirements
1. Telah registrasi akun  wandb (weight and biases) kalau belum pada week ini akan dikupas habis santai ajee wkwk.
2. install library wandb di device masing-masing

## Overview
Sebelum masuk kedalam tahap instalasi wandb, kita coba mengetahui kegunaan dari wandb dari surfacenya (permukaan) aja. wandb sendiri memiliki banyak kegunaan dan umumnya biasa digunakan untuk mentracking dan memvisualisasi hasil model yang telah kita latih. **bahasa bayinya gimana tuh bang??**, kurleb dia bisa nyimpen history apa yang telah kita latih, dan kita bisa mempelajari hasil tuning-an amarineers biar nantinya lebih gacor buat proses inferencing dan proses prediksi nantinya. kita coba sedikit lihat workflow sederhana kita seperti pada figure dibawah :s👇.
<a id="workflow"></a>

![workflow vision sederhana](../../assets/img/image.png)

nah disitu ketika menerima hasil model yang telah kita latih terdapat **3 arah panah**, kita sebagai visioneer setidaknya bisa memahami apa yang telah kita latih. artinya, apabila dirasa sudah mendapatkan hasil yang maksimal bisa langsung di deploy apabila data yang didapat dari hasil training tidak memuaskan bisa diperkaya lagi tuh datanya. terkahir juga untuk mempersingkat waktu dalam proses labeling bisa kita gunakan dari model yang telah kita latih, kurleb begituww 🤗!. Sekarang cuss kita coba proses instalasi dan registrasi 🏃💨:.

## Installation
Pada section ini visioneer bisa langsung buka web wandb lewat tautan biru yang dah kusematin atau lewat google juga bisa. gass kita ulik bareng step-stepnyaww..
<a id="akses_ke_web_wandb"></a>

**1. Akses web [🔗wandb]((https://wandb.auth0.com/login?state=hKFo2SByWVZsV3FmTUdLdHgtdkdQRkNYbV9PdDZkdGxjVkxOVKFupWxvZ2luo3RpZNkgNEs1dC1pdko4MmRoU1dFd0xSaVRUVm02WGJsMEs4REujY2lk2SBWU001N1VDd1Q5d2JHU3hLdEVER1FISUtBQkhwcHpJdw&client=VSM57UCwT9wbGSxKtEDGQHIKABHppzIw&protocol=oauth2&nonce=U2lXcmxXamdycDNRcVUxfg%3D%3D&redirect_uri=https%3A%2F%2Fapi.wandb.ai%2Foidc%2Fcallback&response_mode=form_post&response_type=id_token&scope=openid%20profile%20email&signup=true)) buat signup dulu**
![halaman signup wandb](../../assets/img/image-2.png)
temen temen bisa signup pake akun google universitas yak contoh ub. jadi masukin pake email ub nanti seingetku disuru pake trial dulu 30 hari nanti kalo abis bisa klaim lewat [🔗ini](https://wandb.ai/academic_application.) kalo ga nanti langsung dapet pop up notifikasi buat apply academic research plan :thumbsup

<a id="bikin_project"></a>
**2. Bikin project baru di workspace kalian**
![contoh workspace pic](../../assets/img/image-1.png)
interface nya kurleb awal kek gini bisa beda beda si tapi intinya bisa lanngsung pilih tab **create new project** terus nanti muncul pop up create new project kek figure diatas.

<a id="install_library"></a>
**3. install library wandb dan setup di device**
![contoh punya pic](../../assets/img/image-3.png)
Interface awal kurleb kek figure diatas nah disitu ada tulisan setup wandb library dan cara log a run to new project. visioneer bisa langsung bukak terminal kalo di windows bisa lewat powershell, dan langsung paste ajah di terminalnya nanti otomatis download kek figure dibawah 👇.

![install wandb](../../assets/img/image-4.png)
kalo udah install selanjutnya jalanin command `wandb login` nanti disuruh masukin API_KEY, **ingat API_KEY jangan pernah disebarrr**. kurleb contohnya kek figure dibawah 👇.

![wandb login](../../assets/img/image-5.png)

kalo udah berhasil nanti muncul notifikasi di terminalnya kek figure dibawah 👇.
![success wandb login](../../assets/img/image-6.png)

## Tracking ur Model YOLOv5 and YOLOv8
Nahh, pada section core ini, setelah kita mengsetup seluruhnya kita akan coba mempraktekkan apa yang telah dipelajari di week sebelumnya dan mengevaluasi hasil model yang telah kita latih. bagi visioneer yang bingung dengan week sebelumnya bisa cek [Week-5](/weeks/week-5/README.md) atau di tautan video berikut
[🔗Bisa dicekk singkat koo videonya](https://youtu.be/87c5-ThfW1k).

### YOLOv5 dan YOLOv8
---
Di percobaan tracking pada YOLOv5 kita akan mencoba lewat os masing-masing disini pic contohin lewat ubuntu tapi buat windows aman aja kurleb caranya sama. dan untuk YOLOv8 caranya juga sama seperti YOLOv5.

bisa buka terminalnya lagi ketik command dibawah:
```bash
# branch dari wnb (gausa kalo dah install wandb sebelumnya)
!pip install -q git+https://github.com/wandb/wandb@feat/ultralytics
```

Impor library yang bakal digunakan
```python
import wandb
from wandb.integrations.ultralytics import add_wandb_callback
from ultralytics import YOLO
import os
```

Proses training menggunakan yolov5 dan menyimpannya pada log wandb (wnb)
```python
model = "yolov5nu.pt" # sebagaimana contoh disini pic pake yolov5nu

wandb.init(
  project="vision" #contoh (ini sesuaikan sama nama project kalian yang di web wandb)
  name="yolo-vision-run" #contoh (ini buat nyimpen history runs)
)

# simpen tempat datapath
data_path = "/home/path/kalian/nyimpen/.yaml" # pastikan kalo pake windows depannya kasih "r" sebelum string

if not os.path.exists(data_path):
  print(f"Error: File {data_path} tidak ditemukan. Kamu salah masukin datapath")
  wandb.finish() # setelah init harus di keluarin karna gagal
  exit() #biar ga lanjut ke training model

# kalo mau pake callback nanti bakal dijelasin kenapa pake callback
add_wandb_callback(model, enable_model_checkpointing=True)

# Fine Tuning Model kita
# setiap selesai epoch, hasil prediksi pada validasi akan disimpan di log
# bagusnya wnb ni bisa nampilih table yang interaktif dan mudahin kita gitu lhoh

## bikin try exception buat cegah error
try:
  model.train(
    project="vision-training", # usahakan dibedain namanya sama project yang di wnb biar ga bingung
    data=data_path, #panggil datapath yang udah diinisialisasi di awal
    epochs=5, # ini bebas mau ngatur berapa epochs
    imgsz=640 # defaultnya 640
  )

  model.val()

except Exception as e:
  print(f"Gagal Training: {e}")

finally:
  wandb.finish() # wajib dikeluarin habis menjalankan wandb (wnb)
```

Hasil dari wandb apabila workspacenya dibuka kurang lebih nanti kek gini

![workspace pic](../../assets/img/workspace.gif)

Apabila kita membuka tab runs akan menampilkan model yang telah berhasil di training dan disimpan historynya. ini juga bisa melihat apakah model yang telah dilatih berhasil atau gagal. semua tersimpan di tab ini.

![runs pic](../../assets/img/runs.gif)

Nahh mungkin cukup sampe disini aja buat week kali ini pabila bingung bisa tanyain digrup or u can get in touch with me: https://wildanaziz.vercel.app/


## References
[1] Ultralytics. (n.d.). Train mode. Retrieved June 3, 2025, from https://docs.ultralytics.com/modes/train/  
[2] Ultralytics. (n.d.). Validation mode. Retrieved June 3, 2025, from https://docs.ultralytics.com/modes/val/  
[3] Weight and Biases. (n.d.). Track Experiments. Retrieved June 3, 2025, from https://docs.wandb.ai/tutorials/experiments/  
[4] Weight and Biases. (n.d.). YOLOv5 Integrations Guide. Retrieved June 3, 2025, from https://docs.wandb.ai/guides/integrations/yolov5/  
