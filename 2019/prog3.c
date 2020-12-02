#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>
#include <time.h>

#define SIZE 100001

int main (void)
{
	clock_t begin = clock();

	//char map[SIZE][SIZE] = {0};
	char** map = malloc(SIZE * sizeof *map);
	for (int i = 0; i < SIZE; i++)
	{
		map[i] = malloc(SIZE * sizeof *map[i]);
	}
	int posX = SIZE / 2;
	int posY = SIZE / 2;

	map[posX][posY] = 'S';

	char lineTwoChar = '2';

	char dir;
	int steps;
	while (scanf("%c%d,", &dir, &steps) == 2)
	{
		if (dir == '\n')
		{
			break;
		}

		while (steps--)
		{
			if      (dir == 'R') posX++;
			else if (dir == 'L') posX--;
			else if (dir == 'U') posY--;
			else if (dir == 'D') posY++;

			map[posX][posY] = dir;
			if (steps == 0)
				map[posX][posY] = '+';
		}
	}

	posX = SIZE / 2;
	posY = SIZE / 2;

	unsigned int minSteps = UINT_MAX;
	unsigned int steps1 = 0;
	unsigned int steps2 = 0;

	while (scanf("%c%d,", &dir, &steps) == 2)
	{
		while (steps--)
		{
			if      (dir == 'R') posX++;
			else if (dir == 'L') posX--;
			else if (dir == 'U') posY--;
			else if (dir == 'D') posY++;

			steps2++;

			if (map[posX][posY] == 0)
			{
				map[posX][posY] = lineTwoChar;
			}
			else if(map[posX][posY] != lineTwoChar)
			{
				steps1 = 0;
				int tposX = posX, tposY = posY;
				while (map[tposX][tposY] != 'S')
				{
					if (map[tposX][tposY] == 'U')
					{
						while (map[tposX][tposY] != '+' && map[tposX][tposY] != 'S')
						{
							tposY++;
							steps1++;
						}
						if (map[tposX][tposY] == 'S')
							break;

						if (map[tposX + 1][tposY] == 'L')
						{
							tposX++;
							steps1++;
						}
						else if (map[tposX - 1][tposY] == 'R')
						{
							tposX--;
							steps1++;
						}
					}
					else if (map[tposX][tposY] == 'D')
					{
						while (map[tposX][tposY] != '+' && map[tposX][tposY] != 'S')
						{
							tposY--;
							steps1++;
						}
						if (map[tposX][tposY] == 'S')
							break;

						if (map[tposX + 1][tposY] == 'L')
						{
							tposX++;
							steps1++;
						}
						else if (map[tposX - 1][tposY] == 'R')
						{
							tposX--;
							steps1++;
						}
					}
					else if (map[tposX][tposY] == 'L')
					{
						while(map[tposX][tposY] != '+' && map[tposX][tposY] != 'S')
						{
							tposX++;
							steps1++;
						}
						if (map[tposX][tposY] == 'S')
							break;

						if (map[tposX][tposY + 1] == 'U')
						{
							tposY++;
							steps1++;
						}
						else if (map[tposX][tposY - 1] == 'D')
						{
							tposY--;
							steps1++;
						}
					}
					else if (map[tposX][tposY] == 'R')
					{
						while(map[tposX][tposY] != '+' && map[tposX][tposY] != 'S')
						{
							tposX--;
							steps1++;
						}
						if (map[tposX][tposY] == 'S')
							break;

						if (map[tposX][tposY + 1] == 'U')
						{
							tposY++;
							steps1++;
						}
						else if (map[tposX][tposY - 1] == 'D')
						{
							tposY--;
							steps1++;
						}
					}
					else if (map[tposX][tposY] == '+')
					{
						if (map[tposX + 1][tposY] == 'L')
							tposX++;
						else if (map[tposX - 1][tposY] == 'R')
							tposX--;
						else if (map[tposX][tposY + 1] == 'D')
							tposY++;
						else if (map[tposX][tposY - 1] == 'U')
							tposY--;
						else
							puts("wtf");
					}
					else
						printf("Unknown char: %c (%d)\n", map[tposX][tposY], map[tposX][tposY]);
				}

				if (steps1 + steps2 < minSteps)
					minSteps = steps1 + steps2;
			}
		}
	}


//	puts("Grid:");
//	for (int i = 0; i < SIZE; i++)
//	{
//		for (int j = 0; j < SIZE; j++)
//			printf("%c ", map[j][i] == 0 ? '.' : map[j][i]);
//		putchar('\n');
//	}

	for (int i = 0; i < SIZE; i++)
	{
		free(map[i]);
	}
	free(map);
	printf("Min Steps = %u\n", minSteps);

	clock_t end = clock();
	printf("Time spent: %f\n", (double)(end - begin) / CLOCKS_PER_SEC);
}
