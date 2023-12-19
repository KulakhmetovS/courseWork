#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define MAX_SIZE 500

/*
 Функция, генерирующая псевдорандомом матрицу смежности графа,
 хроматическое число которого требуется найти
*/
void RandGraph(int size)
{
    srand(time(NULL));

    //int **graph;    // Указатель на матрицу смежности
    //int *colors;    // Вектор цветов графа
	
	int graph[MAX_SIZE][MAX_SIZE], colors[MAX_SIZE], used_colors[MAX_SIZE];

    /*graph = (int **)malloc(sizeof(int *) * size);
    for(int i = 0; i < size; i++)
        graph[i] = (int *)malloc(sizeof(int) * size);*/

    // Определение псевдорандомом смежных вершин
    for(int i = 0; i < size; i++)
        for(int j = i; j < size; j++)
        {
            graph[i][j] = rand() % 2;
            graph[j][i] = graph[i][j];
            if(i == j) graph[i][j] = 0;
        }

    //======================================================================
    //colors = (int *)malloc(sizeof(int) * size);
    //======================================================================

    for (int i = 0; i < size; i++)
    {
        // Инициализация множества использованных цветов соседей
        //int *used_colors = (int *)malloc(sizeof(int) * size);
        
        for(int i = 0; i < size; i++)
        	used_colors[i] = 0;
        
        // Проходим по всем соседям текущей вершины и добавляем их цвета в множество
        for (int j = 0; j < size; j++)
        {
            if (graph[i][j] && colors[j] != 0)
            {
                used_colors[colors[j]] = 1;
            }
        }
        // Выбор цвета для текущей вершины
        for (int j = 1; j <= size; j++)
        {
            if (used_colors[j] == 0)
            {
                colors[i] = j;
                break;
            }
        }
        //free(used_colors);
    }

    //======================================================================

    FILE *file;
    file = fopen("data.txt", "w");
    for(int i = 0; i < size; i++)
    {
        for(int j = 0; j < size; j++)
        {
            fprintf(file, "%c", graph[i][j] + '0');
        }
        fprintf(file, "\n");
    }

    for(int i = 0; i < size; i++)
        fprintf(file, "%c", colors[i] + '0');

    fclose(file);

    //free(colors);
    //for(int i = 0; i < size; i++)
    //    free(graph[i]);
    //free(graph);
}
