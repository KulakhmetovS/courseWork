from Graphs import *    # Модуль, реализующий основные функции программы

Window = Tk()   # Инициализация виджета окна
Window.title('Курсовой проект "Хроматическое число графа"') # Заголовок окна
Window.geometry('500x500')  # Размер окна в пикселях

MFrame = Frame()    # Фрейм, отвечающий за текст
DFrame = Frame()    # Фрейм, отвечающий за дату
Frame = Frame() # Фрейм, содержащий кнопки

# Функция завершает цикл обработки окна и ищет хроматическо число рандомно сгенерированного графа
def Random():
    Window.destroy()
    RandomGraph()
# Функция завершает цикл обработки окна и ищет хроматическо число графа, считанного из файла
def File():
    Window.destroy()
    FromFile()

# Метки текста и даты
lb0 = Label(MFrame, text='Министерство образования Российской Федерации')
lb1 = Label(MFrame, text='Пензенский государственный университет')
lb2 = Label(MFrame, text='Кафедра "Вычислительная техника"\n\n\n\n')
lb3 = Label(MFrame, text='Курсовой проект')
lb4 = Label(MFrame, text='по курсу "Логика и основы алгоритмизации \nв инженерных задачах"')
lb5 = Label(MFrame, text='на тему "Разрабтка алгоритма нахождения \nхроматического числа графа"\n\n')
lb6 = Label(MFrame, text='Выполнил:\t\n\tстудент группы 22ВВВ3\nКулахметов С.И.\n\nПриняли:\t\n\t'\
                                    'к.э.н доцент Акифьев И.В.\n\tк.т.н. доцент Юрова О.В.')
lb7 = Label(DFrame, text='\n\n\nПенза 2023')
# Кнопки
BTN1 = Button(Frame, text="Сгенерировать граф", command=Random)
BTN2 = Button(Frame, text="Считать граф из файла", command=File)
btnExit = Button(Frame, text="Завершить", command=exit)

# Относительные позиции меток и кнопок
lb0.pack(side=TOP)
lb1.pack(side=TOP)
lb2.pack(side=TOP)
lb3.pack(side=TOP)
lb4.pack(side=TOP)
lb5.pack(side=TOP)
lb6.pack(side=RIGHT)
lb7.pack()
BTN1.pack(side=LEFT)
BTN2.pack(side=RIGHT)

# Позиции фреймов
btnExit.pack(side=RIGHT)
MFrame.pack(side=TOP)
DFrame.pack()
Frame.pack(side=BOTTOM)

# Цикл обработки событий окна
Window.mainloop()
