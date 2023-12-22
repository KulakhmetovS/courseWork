import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from ctypes import *
from tkinter import *
import tkinter.messagebox as box
from Colors import *

Random_Graph_Matrix = CDLL('./RandGraph.so')
Read_From_File_Matrix = CDLL('./ReadFromFile.so')

def RandomGraph():
    window = Tk()
    window.title("Хроматическое число графа")
    window.geometry("450x100")

    frame = Frame()
    entry = Entry(frame)

    def dialog():
        global size

        #Обработка исключений
        try:    #В данном случае проверка на возможность конвертации в int
            number=int(entry.get())
        except ValueError:  #Если значение - char, string или float, то выходит предупреждение
            box.showerror('Некорректные данные', 'Некорректные введённые данные: число вершин '\
                                    'должно быть целым и положительным')
            exit()

        size = number

        if size<1:
            box.showerror('Некорректные данные', 'Некорректные введённые данные: число '\
                                    'вершин должно быть положительным и не равным 0')
            exit()
        elif size>20:
            box.showerror('Некорректные данные', 'Слишком большое число вершин: '\
                                                 'предпочтительно генерировать не более 20 вершин')
            exit()

        window.destroy()

    btn = Button(frame, text="Enter", command=dialog)
    lb = Label(frame, text="Введите количество вершин: ")

    lb.pack(side=LEFT)
    entry.pack(side=LEFT)
    btn.pack(side=RIGHT)
    frame.pack()

    window.mainloop()

    Random_Graph_Matrix.RandGraph(c_int(size))

    # Чтение данных из файла
    f = open('data.txt', 'r', encoding='utf-8')
    data = f.read() # Чтение строки с данными
    f.close()

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

    # инициализация вектора цветов для покраски графа
    Spectral = ['white'] * size

    ColorsInit(colors, Spectral, size)  #Задание цветов для вершин

    # непосредственное рисование графа
    G = nx.DiGraph(np.matrix(mas))
    nx.draw(G, node_color=Spectral, with_labels=True, node_size=600, arrows=False)
    plt.show()

##############################################################################

def FromFile():
    window = Tk()
    window.title("Хроматическое число графа")
    window.geometry("450x100")

    frame = Frame(window)
    entry = Entry(frame)
    def dialog():
        global s
        s = entry.get()

        try:
            fl = open(entry.get(), "r", encoding='utf-8')
        except FileNotFoundError:
            box.showerror('Ошибка при работе с файлом', 'Файл отсутствует или неккоректно введено ' \
                                                 'имя файла')
            exit()

        result = os.stat(entry.get())
        if result.st_size==0:
            box.showerror('Некорректные данные', 'Файл пуст')
            exit()
        fl.close()


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

            try:
                Mas[i][j] = int(Data[k])
            except ValueError:  # Если значение - char, string или float, то выходит предупреждение
                box.showerror('Некорректные данные', 'Некорректные введённые данные в файле')
                exit()
            except IndexError:
                box.showerror('Некорректные данные', 'Некорректные введённые данные в файле')
                exit()

            k += 1

            try:
                if Data[k] == '\n':
                    k += 1
            except IndexError:
                box.showerror('Некорректные данные', 'Некорректные введённые данные в файле')
                exit()

    # Считывание вектора цветов из файла
    for i in range(0, size):
        try:
            Colors[i] = int(Data[k])
        except ValueError:  # Если значение - char, string или float, то выходит предупреждение
            box.showerror('Некорректные данные', 'Некорректные введённые данные в файле')
            exit()
        except IndexError:
            box.showerror('Некорректные данные', 'Некорректные введённые данные в файле')
            exit()
        k += 1

    # инициализация вектора цветов для покраски графа
    ColorsInit(Colors, spectral, size)

    # непосредственное рисование графа
    Gr = nx.DiGraph(np.matrix(Mas))
    nx.draw(Gr, node_color=spectral, with_labels=True, node_size=600, arrows=False)
    plt.show()