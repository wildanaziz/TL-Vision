# PENGERJAAN POIN 3️⃣
## Prediksi Poin 1 (MLP)
Dengan menambahkan program di bawah ini pada program poin-1, maka kita dapat memprediksi hasil dari algoritma `MultiLayer Perceptron (MLP)`
```
predicted_label = predict(sample_image, W1, b1, W2, b2)[0]

print(f"Label sebenarnya: {true_label}")
print(f"Prediksi model:   {predicted_label}")



def show_image(image_vector):
    plt.imshow(image_vector.reshape(28, 28), cmap='gray')
    plt.axis('off')
    plt.show()

show_image(sample_image)
```

## Prediksi Poin 2 (CNN)
Dengan menambahkan program di bawah ini pada program poin-2, maka kita dapat memprediksi hasil dari algoritma `Convolutional Neural Network (CNN)`
```
def show_predictions(model, x_data, y_true, num_samples=10):
    predictions = model.predict(x_data[:num_samples])  # prediksi probabilitas
    predicted_labels = np.argmax(predictions, axis=1)  # ambil label dengan probabilitas tertinggi

    plt.figure(figsize=(15, 5))
    for i in range(num_samples):
        plt.subplot(2, num_samples // 2, i + 1)
        plt.imshow(x_data[i].reshape(28, 28), cmap='gray')
        plt.title(f"True: {y_true[i]}\nPred: {predicted_labels[i]}")
        plt.axis('off')
    plt.suptitle("Prediksi vs Label Asli", fontsize=16)
    plt.tight_layout()
    plt.show()
show_predictions(model, x_test, y_test, num_samples=10)
```

# Perbandingan MLP dengan CNN
CNN lebih unggul dari segi akurasi karena dapat memproses citra dengan lebih baik. Namun, MLP masih dapat digunakan untuk kasus-kasus tertentu di mana data citra tidak terlalu kompleks, yang dimana program dapat dijalankan lebih cepat dibandingkan CNN.