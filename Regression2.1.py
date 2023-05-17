import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Logistic regression using loops

# definition of the sigmoid function
def sigmoid(z):
    f = 1 / (1 + (np.e) ** -z)
    return f


# cost
def cost(x, y, w, b):
    m, n = x.shape
    cost = 0

    for i in range(m):
        cost_i = (-y[i] * (np.log(sigmoid(np.dot(w, x[i])) + b))) - (
                    (1 - y[i]) * (np.log(1 - sigmoid(np.dot(w, x[i])) + b)))
        cost += cost_i

    return cost / m


# gradient(derivatives)
def gradient(x, y, w, b):
    m, n = x.shape
    dj_dw = np.zeros(n)  # derivative terms for each feature
    dj_db = 0.

    for i in range(m):
        z_wb = np.dot(w, x[i]) + b
        f_wb = sigmoid(z_wb)

        for j in range(n):
            dj_dw[j] += (f_wb - y[i]) * x[i][j]
        dj_db += f_wb - y[i]

    dj_dw = dj_dw / m
    dj_db = dj_db / m

    return dj_dw, dj_db


# gradient descent
def gradient_descent(x, y, w_in, b_in, alpha, num_iters):
    m, n = x.shape
    w = w_in
    b = b_in
    for i in range(num_iters):
        dj_dw, dj_db = gradient(x, y, w, b)

        w = w - alpha * dj_dw
        b = b - alpha * dj_db

    return w, b


# predicting
def predict(x, w, b):
    m, n = x.shape
    p = np.zeros(m)

    for i in range(m):
        z_wb = np.dot(w, x[i]) + b
        f_wb = sigmoid(z_wb)

        if (p[i] >= 0.5):
            p[i] = 1
        else:
            p[i] = 0

    return p


# preprocessing
dataset = pd.read_csv("ex2data1.csv")
x_train = dataset.iloc[:, :-1].values
y_train = dataset.iloc[:, -1].values
y_train = y_train.reshape(len(y_train), 1)

# initialization
m, n = x_train.shape
w = np.zeros(n)
b = 0.

w_out, b_out = gradient_descent(x_train, y_train, w, b, 1e-4, 10000)

print(w_out)
print(b_out)

# predicting
y_pred = predict(x_train, w_out, b_out)