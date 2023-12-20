import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from ctypes import *
from tkinter import *

#Загружаем библиотеку на С
Random_Graph_Matrix = CDLL('./RandGraph.so')
Read_From_File_Matrix = CDLL('./ReadFromFile.so')
'''
number = 0

window = Tk()
window.title("Хроматическое число графа")
window.geometry("450x100")

frame = Frame(window)
entry = Entry(frame)
def dialog():
    global size
    number=int(entry.get())
    size = number
    window.destroy()

btn = Button(frame, text="Enter", command=dialog)
lb = Label(frame, text="Введите количество вершин: ")

lb.pack(side=LEFT)
entry.pack(side=LEFT)
btn.pack(side=RIGHT)
frame.pack()

window.mainloop()
#print('Введите число вершин')
#size = int(input())
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

# инициализация вектора цветов для покраски графа
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

# непосредственное рисование графа
G = nx.DiGraph(np.matrix(mas))
nx.draw(G, node_color=Spectral, with_labels=True, node_size=600, arrows=True)
plt.show()

##############################################################################
'''
window = Tk()
window.title("Хроматическое число графа")
window.geometry("450x100")

frame = Frame(window)
entry = Entry(frame)
def dialog():
    global s
    s = entry.get()
    file = open('filename.txt', 'w', encoding='utf-8')
    file.write(entry.get())
    file.close()
    window.destroy()

btn = Button(frame, text="Enter", command=dialog)
lb = Label(frame, text="Введите имя файла: ")

lb.pack(side=LEFT)
entry.pack(side=LEFT)
btn.pack(side=RIGHT)
frame.pack()

window.mainloop()
#print('Введите число вершин')
#size = int(input())
#Из-за ограничений работы с памятью, больше 5 вершин корректно сгенерировать проблематично
size=Read_From_File_Matrix.ReadFromFile()

# Чтение данных из файла
f = open(s, 'r', encoding='utf-8')
Data = f.read() # Чтение строки с данными
f.close()

Mas = [0] * size    # Матрица смежности, считываемая из файла
for i in range(size):
    Mas[i] = [0] * size
Colors = [0] * size
spectral = ['white'] * size

k = int(0)
# Считывание матрицы смежности из файла
for i in range(0, size):
    for j in range(0, size):
        Mas[i][j] = int(Data[k])
        k += 1
        if Data[k] == '\n':
            k += 1

# Считывание вектора цветов из файла
for i in range(0, size):
    Colors[i] = int(Data[k])
    k += 1

# инициализация вектора цветов для покраски графа
for i in range(0, size):
    if Colors[i] == 0:
        spectral[i] = 'white'
    elif Colors[i] == 1:
        spectral[i] = 'red'
    elif Colors[i] == 2:
        spectral[i] = 'yellow'
    elif Colors[i] == 3:
        spectral[i] = 'green'
    elif Colors[i] == 4:
        spectral[i] = 'blue'
    elif Colors[i] == 5:
        spectral[i] = 'orange'

# непосредственное рисование графа
Gr = nx.DiGraph(np.matrix(Mas))
nx.draw(Gr, node_color=spectral, with_labels=True, node_size=600, arrows=True)
plt.show()
