import numpy as np

def load_data():
    data = np.loadtxt("data/data.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y