import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Vectorized implementation of logistic regression

# sigmoid function
def sigmoid(z):
    a = 1 / (1 + np.exp(-z))

    return a


# predicted y value for a given w,b ans x
def y_out(x_test, w_ini, b_ini):
    m, n = x_test.shape
    a = sigmoid(np.dot(w_ini, np.transpose(x_test)) + b_ini)
    a = a.reshape(m, 1)
    return a


# loss of a single training example
def loss(x_train, y_train, w_ini, b_ini):
    l = 0
    l = -(y * np.log(y_out(x_train, w_ini, b_ini)) + (1 - y) * np.log(1 - y_out(x_train, w_ini, b_ini)))

    return l


# the cost function
def cost(x, y, w, b):
    J = 0
    m, n = x.shape
    J = (1 / m) * np.sum(loss(x, y, w, b))

    return J


# derivative terms
def gradient(x_train, y_train, w_ini, b_ini):
    m, n = x_train.shape
    dw = np.zeros(n)
    dw = dw.reshape(len(dw), 1)
    db = 0.

    dw = (1 / m) * (np.dot(np.transpose(x_train), y_out(x_train, w_ini, b_ini) - y_train))
    db = (1 / m) * (np.sum(y_out(x_train, w_ini, b_ini) - y_train))

    dw = dw.reshape(1, len(dw))
    return dw, db


# gradient descent
def optimize(x_train, y_train, w_ini, b_ini, alpha, itirations):
    m, n = x.shape
    w = w_ini
    b = b_ini
    for i in range(itirations):
        dw, db = gradient(x_train, y_train, w, b)
        w = w - alpha * (dw)
        b = b - alpha * (db)

    return w, b


dataset = pd.read_csv("ex2data1.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
y = y.reshape(len(y), 1)
m, n = x.shape

# initialization
w = np.zeros(n)
b = 0.

# running the algoritm
w_out, b_out = optimize(x, y, w, b, 1e-5, 10000)

# parameters after running gradient descent
print(w_out, b_out)