# -- coding: utf-8 --
"""CNN dengan Dataset dari CSV via Pandas"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load dataset dari file CSV
# Ganti 'dataset.csv' dengan nama file CSV kamu
data = pd.read_csv(r'F:\FILKOM\robotiik\TL-Vision\weeks\week-4\fashion-mnist_train.csv')  # contoh nama file

# Pisahkan label dan fitur
y = data.iloc[:, 0].values             # kolom pertama = label
X = data.iloc[:, 1:].values / 255.0    # normalisasi piksel ke [0, 1]

# Ubah bentuk jadi (28, 28, 1) untuk CNN
X = X.reshape(-1, 28, 28, 1)

# Bagi data jadi train dan test
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bangun model CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Latih model
history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_test, y_test),
                    verbose=2)

# Evaluasi model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Akurasi CNN pada data uji: {test_acc:.4f}")

# Konversi hasil ke DataFrame
history_df = pd.DataFrame(history.history)
print("\nRingkasan Hasil Training:")
print(history_df)

# Visualisasi dari DataFrame
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
history_df[['accuracy', 'val_accuracy']].plot(ax=plt.gca())
plt.title('Akurasi Pelatihan vs Validasi')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True)

plt.subplot(1, 2, 2)
history_df[['loss', 'val_loss']].plot(ax=plt.gca())
plt.title('Loss Pelatihan vs Validasi')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)

plt.tight_layout()
plt.show()
