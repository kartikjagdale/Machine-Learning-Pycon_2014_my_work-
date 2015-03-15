import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
#print iris.data

def plot_iris(x, y):
    #formator to label the colorbar with the targer name
    formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])
    plt.scatter(iris.data[:, x], iris.data[:, y],c=iris.target)
    plt.colorbar(ticks=[0,1,2],format=formatter)
    plt.xlabel(iris.feature_names[x])
    plt.ylabel(iris.feature_names[y])

plot_iris(3,3)
plt.show()
