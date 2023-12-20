#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_SIZE 500

int ReadFromFile()
{	
	char filename[80];
    int graph[MAX_SIZE][MAX_SIZE];
    int size;
    int colors[MAX_SIZE], used_colors[MAX_SIZE];

    //=======================================================

    FILE *file, *name;
    int count = 0, k = 0;
    char c, arr[MAX_SIZE * 2];
	
	name = fopen("filename.txt", "r");
	fscanf(name, "%s", filename);
	fclose(name);
	
    file = fopen(filename, "r");

    while((c = fgetc(file)) != EOF)
        count++;

    rewind(file);

    for(int i = 0; i < count; i++)
        arr[i] = fgetc(file);

    size = 0;
    while(arr[size] != '\n')
        size++;

    for(int i = 0; i < size; i++)
    {
        for(int j = 0; j < size; j++)
        {
            graph[i][j] = arr[k];
            k++;
            if(arr[k] == '\n') k++;
            graph[i][j] = graph[i][j] - 48;
        }
    }

    fclose(file);

    //=======================================================

    for(int i = 0; i < size; i++)
        colors[i] = 0;

    //=======================================================

    for (int i = 0; i < size; i++)
    {
        // инициализация множества использованных цветов соседей
        for(int i = 0; i < size; i++)
            used_colors[i] = 0;
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

    //========================================================

    file = fopen(filename, "a");

    for(int i = 0; i < size; i++)
        fprintf(file, "%c", colors[i] + 48);

    fclose(file);
    
    return size;
}
