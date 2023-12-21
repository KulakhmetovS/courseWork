from Graphs import *

Window = Tk()
Window.title('Курсовой проект "Хроматическое число графа"')
Window.geometry('500x600')

MFrame = Frame()
Frame = Frame()
def Random():
    Window.destroy()
    RandomGraph()
def File():
    Window.destroy()
    FromFile()

lb0 = Label(MFrame, text='Министерство образования Российской Федерации')
lb1 = Label(MFrame, text='Пензенский государственный университет')
lb2 = Label(MFrame, text='Кафедра "Вычислительная техника"\n\n\n\n')
lb3 = Label(MFrame, text='Курсовой проект')
lb4 = Label(MFrame, text='по курсу "Логика и основы алгоритмизации \nв инженерных задачах"')
lb5 = Label(MFrame, text='на тему "Разрабтка алгоритма нахождения \nхроматического числа графа"\n\n')
lb6 = Label(MFrame, text='Выполнил\t\n')

BTN1 = Button(Frame, text="Сгенерировать граф", command=Random)
BTN2 = Button(Frame, text="Считать граф из файла", command=File)
btnExit = Button(Frame, text="Завершить", command=exit)

lb0.pack(side=TOP)
lb1.pack(side=TOP)
lb2.pack(side=TOP)
lb3.pack(side=TOP)
lb4.pack(side=TOP)
lb5.pack(side=TOP)
lb6.pack(side=RIGHT)
BTN1.pack(side=LEFT)
BTN2.pack(side=RIGHT)
btnExit.pack(side=BOTTOM)
MFrame.pack(side=TOP)
Frame.pack(side=BOTTOM)


Window.mainloop()

