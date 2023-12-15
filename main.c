#include <stdio.h>
#include <stdlib.h>

int **Creategraph(int **, int); // Функция для генерирования графа
void GraphColors(int **, int *, int);   //Функция для раскрашивания графа
int ColorNumber(int *, int);    // Функция для нахождения хроматического числа

int main() {
    int size = 0; // количество вершин в графе
    int **graph = NULL; // Указатель на матрицу смежности графа
    int *colors;    // Указатель на вектор цветов

    printf("Введите количество вершин в графе: ");
    scanf("%d", &size);

    colors = (int *)malloc(sizeof(int) * size);    // Выделение памяти под вектор цветов

    graph = Creategraph(graph, size);

    // Вывод матрицы смежности графа
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }

    GraphColors(graph, colors, size);

    // вывод результатов раскраски
    printf("Раскраска графа:\n");
    for (int i = 0; i < size; i++) {
        printf("Вершина %d - цвет %d\n", i+1, colors[i]);
    }

    int number = ColorNumber(colors, size);
    printf("Хроматическое число графа = %d", number);

    // Освобождение памяти
    for(int i = 0; i < size; i++)
        free(graph[i]);
    free(graph);

    free(colors);

    return 0;
}

int** Creategraph(int **graph, int size)
{
    srand(time(NULL));

    int i = 0, j = 0;

    // Выделение памяти под матрицу смежности графа
    graph = (int **)(malloc(sizeof(int *) * size));
    for(i = 0; i < size; i++)
        graph[i] = (int *)(malloc(sizeof(int *) * size));

    // Определение псевдорандомом смежных вершин
    for(i = 0; i < size; i++)
        for(j = i; j < size; j++)
        {
            graph[i][j] = rand() % 2;
            graph[j][i] = graph[i][j];
            if(i == j) graph[i][j] = 0;
            if(graph[i][j] == 1);
        }

    return graph;   // Возвращение указателя на полученную матрицу смежности
}

void GraphColors(int **graph, int *colors, int size)
{
    for (int i = 0; i < size; i++)
    {
        // инициализация множества использованных цветов соседей
        int *used_colors = (int *)malloc(sizeof(int) * size);
        // проходим по всем соседям текущей вершины и добавляем их цвета в множество
        for (int j = 0; j < size; j++)
        {
            if (graph[i][j] && colors[j] != 0)
            {
                used_colors[colors[j]] = 1;
            }
        }
        // выбор цвета для текущей вершины
        for (int j = 1; j <= size; j++)
        {
            if (used_colors[j] == 0)
            {
                colors[i] = j;
                break;
            }
        }
    }
}

int ColorNumber(int *colors, int size)
{
    int number = 0;

    for(int i = 0; i < size; i++)
        if(number < colors[i]) number = colors[i];  //Находим наибольший индекс цвета

    return number;
}
