from ctypes import *
#Загружаем библиотеку на С
Random_Graph_Matrix = CDLL('./RandGraph.so')
print('Введите число вершин')
a = int(input())
#Из-за ограничений работы с памятью, больше 5 вершин корректно сгенерировать проблематично
Random_Graph_Matrix.RandGraph(c_int(a))

# Чтение данных из файла
f = open('data.txt', 'r', encoding='utf-8')
data = f.read() # Чтение строки с данными
f.close()
print(data)

#res_int = adder.add_int(4, 5)
#print("Сумма 4 и 5 = ", res_int)

#a = c_float(2.5)
#b = c_float(17.9)
#add_float = adder.add_float
#add_float.restype = c_float

#print("Сумма 2.5 и 17.9 = ", add_float(a, b))
