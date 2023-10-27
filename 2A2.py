import numpy as np
#define a sigmoid function
def sm(x):
    return 1 / (1 + np.exp(-x))
def sm_derivative(x):
    return x * (1 - x)
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])
np.random.seed(42)
w0 = 2 * np.random.random((2, 4)) - 1
w1 = 2 * np.random.random((4, 1)) - 1
epochs = 10000
for epoch in range(epochs):
    l0 = inputs
    l1 = sm(np.dot(l0, w0))
    l2 = sm(np.dot(l1, w1))
    layer2_error = outputs - l2
    layer2_delta = layer2_error * sm_derivative(l2)
    layer1_error = layer2_delta.dot(w1.T)
    layer1_delta = layer1_error * sm_derivative(l1)
    w0=2*np.random.random((2,4))-1
    w1=2*np.random.random((4,1))-1
    w1+=l1.T.dot(layer2_delta)
    w0+=l0.T.dot(layer1_delta)
ti=np.array([[0,0],[0,1],[1,0],[1,1]])
pr=sm(np.dot(sm(np.dot(ti,w0)),w1))
pr=np.round(pr)
for i in range(len(ti)):
    print(f"Input:{ti[i]},Estimated Output: {pr[i]}")