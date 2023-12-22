import os   # Модуль для взаимодействия с ОС и файловой системой
import networkx as nx   # Модуль для рисования графа
import numpy as np  # Модуль для математических операций
import matplotlib.pyplot as plt
from ctypes import *    # Модуль для поддержки типов данных языка С
from tkinter import *   # #одуль для отображения графического интерфейса
from tkinter.messagebox import showerror    # Модуль для диалоговых окон
from Colors import *    # Модуль для преобразования числового ветора цветов в их строковые обозначения

# Подключение динамических библиотек, написанных на языке С, и реализующих основной алгоритм программы
Random_Graph_Matrix = CDLL('./RandGraph.so')
Read_From_File_Matrix = CDLL('./ReadFromFile.so')

# Функция нахождения хроматического числа рандомно сгенерированного графа
def RandomGraph():
    window = Tk()   # Инициализация виджета окна
    window.title("Хроматическое число графа")   # Заголовок окна
    window.geometry("450x100")  # Размер окна в пикселях

    frame = Frame() # Фрейм для элементов окна
    entry = Entry(frame)    # Поле ввода значения

    # Функция получения количества вершин графа из поля ввода
    def dialog():
        global size # Глобальная переменная, отвечающая за количество вершин графа

        #Обработка исключений
        try:    #В данном случае проверка на возможность конвертации в int
            number=int(entry.get())
        except ValueError:  #Если значение - char, string или float, то выходит предупреждение
            # Диалоговое окно, сообщающее об ошибке
            showerror('Некорректные данные', 'Некорректные введённые данные: число вершин '\
                                    'должно быть целым и положительным')
            exit()  # Выход из программы

        size = number   # Если всё хорошо, то сохраняем полученное число вершин

        if size<1:  # Если число вершин отрицательное, то граф генерировать не будем
            showerror('Некорректные данные', 'Некорректные введённые данные: число '\
                                    'вершин должно быть положительным и не равным 0')
            exit()
        elif size>20:   # Слишком большое число вершин тоже не нужно, для корректности отображения
            showerror('Некорректные данные', 'Слишком большое число вершин: '\
                                                 'предпочтительно генерировать не более 20 вершин')
            exit()

        window.destroy()    # Выход из цикла обработки событий окна

    btn = Button(frame, text="Enter", command=dialog)   # Кнопка, ответственная за подтверждение ввода данных
    lb = Label(frame, text="Введите количество вершин: ")   # Метка с текстом возле поля ввода

    # Относительные расположения элементов
    lb.pack(side=LEFT)
    entry.pack(side=LEFT)
    btn.pack(side=RIGHT)
    # Отображение фрейма
    frame.pack()

    # Цикл обработки событий окна
    window.mainloop()

    # Вызов функции из динамической библиоткети для генерации и раскрашивания графа
    Random_Graph_Matrix.RandGraph(c_int(size))

    # Чтение данных из обменного файла
    f = open('data.txt', 'r', encoding='utf-8')
    data = f.read() # Чтение строки с данными
    f.close()   # Закрытие файла

    k = int(0)  # Инициализация удополнительное индексной перемнной
    mas = [0] * size    # Матрица смежности, считываемая из файла
    for i in range(size):
        mas[i] = [0] * size
    colors = [0] * size # Вектор цветов, считываемый из файла

    # Считывание матрицы смежности из файла
    for i in range(size):
        for j in range(size):
            mas[i][j] = int(data[k])    # Преобразование строки в int
            k += 1
            if data[k] == '\n':
                k += 1

    # Считывание вектора цветов из файла
    for i in range(size):
        colors[i] = int(data[k])    # Вектор цветов дополнительно дозаписан в файле для обмена данными
        k += 1

    # Инициализация вектора цветов для покраски графа
    Spectral = ['white'] * size

    ChrNumber = int(0)  #Хроматическое число
    ChrNumber = ColorsInit(colors, Spectral, size)  #Задание цветов для вершин

    # непосредственное рисование графа
    G = nx.DiGraph(np.matrix(mas))  # Рисование графа по матрице смежности при помощи модуля networkx
    nx.draw(G, node_color=Spectral, with_labels=True, node_size=600, arrows=False)  # Опции рисования графа

    Str = 'Хроматическое число графа = ' + str(ChrNumber)   # Строка для отображения хроматического числа
    fig = plt.gcf() # Получение рисуемого объекта
    fig.canvas.manager.set_window_title(Str)    # Назначение заголовка окна рисуемому объекту

    plt.show()  # Отображение окна с полем, содержащим граф

##############################################################################

def FromFile():
    window = Tk()
    window.title("Хроматическое число графа")
    window.geometry("450x100")

    frame = Frame(window)
    entry = Entry(frame)

    # Вложенная функция для обработки полученного имени файла
    def dialog():
        global s    # Глобальная переменная, хранящая название файла с расширением
        s = entry.get() # Получение имени файла из поля ввода

        # Обработка исключений и ошибок
        try:    # Проверка на существование файла
            fl = open(entry.get(), "r", encoding='utf-8')
        except FileNotFoundError:
            showerror('Ошибка при работе с файлом', 'Файл отсутствует или неккоректно введено ' \
                                                 'имя файла')
            exit()

        # Проверка содержания файла
        result = os.stat(entry.get())
        if result.st_size==0:   # Если файл пуст, завершение работы алгоритма
            showerror('Некорректные данные', 'Файл пуст')
            exit()
        fl.close()


        file = open('filename.txt', 'w', encoding='utf-8')  # Открытие обменного файла
        file.write(entry.get()) # Запись имени целевого файла в обменный
        file.close()
        window.destroy()

    btn = Button(frame, text="Enter", command=dialog)
    lb = Label(frame, text="Введите имя файла: ")

    lb.pack(side=LEFT)
    entry.pack(side=LEFT)
    btn.pack(side=RIGHT)
    frame.pack()

    window.mainloop()

    '''
    Вызов функции из динамической библиотеки,которая ответственна за раскрашивание графа, 
    считанного из целевого файла, получение возвращаемого значения количества вершин
    '''
    size=Read_From_File_Matrix.ReadFromFile()

    # Открыетие целевого файла
    f = open(s, 'r', encoding='utf-8')

    Data = f.read() # Чтение строки с данными
    f.close()

    Mas = [0] * size    # Матрица смежности, считываемая из файла
    for i in range(size):
        Mas[i] = [0] * size
    Colors = [0] * size # Считываемый вектор цветов
    spectral = ['white'] * size # Вектор цветов для раскрашивания

    k = int(0)
    # Считывание матрицы смежности из файла
    for i in range(0, size):
        for j in range(0, size):

            try:    # Проверка на целочисленное значение ребра считываеого графа
                Mas[i][j] = int(Data[k])
            except ValueError:  # Если значение - char, string или float, то выходит предупреждение
                showerror('Некорректные данные', 'Некорректные введённые данные в файле')
                exit()
            # Если граф имеет неправильную форму, то индекс выйдет за пределы гипотетической матрицы
            except IndexError:
                showerror('Некорректные данные', 'Некорректные введённые данные в файле')
                exit()
            k += 1

            try:
                if Data[k] == '\n':
                    k += 1
            except IndexError:
                showerror('Некорректные данные', 'Некорректные введённые данные в файле')
                exit()

    # Считывание вектора цветов из файла
    for i in range(0, size):
        try:    # Проверка на целочисленность значений вектора цветов
            Colors[i] = int(Data[k])
        except ValueError:  # Если значение - char, string или float, то выходит предупреждение
            showerror('Некорректные данные', 'Некорректные введённые данные в файле')
            exit()
        # Если вектор цветов сбит из-за неправильной формы графа, то индекс выйдет за пределы вектора
        except IndexError:
            showerror('Некорректные данные', 'Некорректные введённые данные в файле')
            exit()
        k += 1

    # Инициализация хроматического числа графа и вызов функции преобразования вектора цветов
    chrNumber = int(0)
    chrNumber = ColorsInit(Colors, spectral, size)

    # Непосредственное рисование графа
    Gr = nx.DiGraph(np.matrix(Mas))
    nx.draw(Gr, node_color=spectral, with_labels=True, node_size=600, arrows=False)

    Str = 'Хроматическое число графа = ' + str(chrNumber)
    fig = plt.gcf()
    fig.canvas.manager.set_window_title(Str)

    plt.show()
