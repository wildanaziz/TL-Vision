import numpy as np
import pandas as pd

data = pd.read_csv('fashion-mnist_train.csv')
data = np.array(data)
np.random.shuffle(data)

# Preprocessing
m, n = data.shape
data_features = data[0:1000].T
Y_features = data_features[0]
X_features = data_features[1:n] / 255

data_labels = data[1000:m].T
Y_train = data_labels[0]
X_train = data_labels[1:n] / 255

# One-hot encoding
def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    return one_hot_Y.T

# Activation functions
def ReLU(Z): return np.maximum(Z, 0)
def dReLU(Z): return Z > 0
def softmax(Z): return np.exp(Z) / sum(np.exp(Z))

# Initialize parameters
def init_params():
    W1 = np.random.rand(128, 784) - 0.5
    b1 = np.random.rand(128, 1) - 0.5
    W2 = np.random.rand(10, 128) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2

# Forward propagation
def forward(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

# Backward propagation
def backward(Z1, A1, Z2, A2, W1, W2, X, Y):
    m = Y.size
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2, axis=1, keepdims=True)

    dZ1 = W2.T.dot(dZ2) * dReLU(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1, axis=1, keepdims=True)

    return dW1, db1, dW2, db2

# Update parameters
def update(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 -= alpha * dW1
    b1 -= alpha * db1
    W2 -= alpha * dW2
    b2 -= alpha * db2
    return W1, b1, W2, b2

# Accuracy check
def get_predictions(A2): return np.argmax(A2, axis=0)
def get_accuracy(predictions, Y): return np.sum(predictions == Y) / Y.size

# Training loop
def train(X, Y, epochs, alpha):
    W1, b1, W2, b2 = init_params()
    for i in range(epochs):
        Z1, A1, Z2, A2 = forward(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)

        if i % 10 == 0:
            predictions = get_predictions(A2)
            acc = get_accuracy(predictions, Y)
            print(f"Epoch {i}: Accuracy = {acc:.3f}")
    return W1, b1, W2, b2

# training
W1, b1, W2, b2 = train(X_train, Y_train, epochs=100, alpha=0.1)