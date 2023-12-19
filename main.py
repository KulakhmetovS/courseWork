import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from ctypes import *
#Загружаем библиотеку на С
Random_Graph_Matrix = CDLL('./RandGraph.so')
print('Введите число вершин')
size = int(input())
#Из-за ограничений работы с памятью, больше 5 вершин корректно сгенерировать проблематично
Random_Graph_Matrix.RandGraph(c_int(size))

# Чтение данных из файла
f = open('data.txt', 'r', encoding='utf-8')
data = f.read() # Чтение строки с данными
f.close()
print(data)


k = int(0)
mas = [0] * size    # Матрица смежности, считываемая из файла
for i in range(size):
    mas[i] = [0] * size
colors = [0] * size # Вектор цветов, считываемый из файла

# Считывание матрицы смежности из файла
for i in range(size):
    for j in range(size):
        mas[i][j] = int(data[k])
        k += 1
        if data[k] == '\n':
            k += 1

# Считывание вектора цветов из файла
for i in range(size):
    colors[i] = int(data[k])
    k += 1

print(mas, colors)

Spectral = ['white'] * size

for i in range(0, size):
    if colors[i] == 0:
        Spectral[i] = 'white'
    elif colors[i] == 1:
        Spectral[i] = 'red'
    elif colors[i] == 2:
        Spectral[i] = 'yellow'
    elif colors[i] == 3:
        Spectral[i] = 'green'
    elif colors[i] == 4:
        Spectral[i] = 'blue'
    elif colors[i] == 5:
        Spectral[i] = 'orange'
'''
options = {
    'node_color': Spectral[5],  # first 5 colors from the Spectral palette
}
'''
G = nx.DiGraph(np.matrix(mas))
nx.draw(G, node_color=Spectral, with_labels=True, node_size=600, arrows=True)
plt.show()

#res_int = adder.add_int(4, 5)
#print("Сумма 4 и 5 = ", res_int)

#a = c_float(2.5)
#b = c_float(17.9)
#add_float = adder.add_float
#add_float.restype = c_float

#print("Сумма 2.5 и 17.9 = ", add_float(a, b))
