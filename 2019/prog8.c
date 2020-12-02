#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

#define ROWS 6
#define COLS 25

int main(void)
{
	int result;
	int minZeros = INT_MAX;

	int image[ROWS][COLS];
	for (int i = 0; i < ROWS; i++)
		for (int j = 0; j < COLS; j++)
			image[i][j] = 2;

	bool endLoop = false;

	for (;;)
	{
		int zeros = 0, ones = 0, twos = 0;
		for (int i = 0; i < ROWS; i++)
		{
			for (int j = 0; j < COLS; j++)
			{
				int bit;
				if (scanf("%1d", &bit) == EOF)
				{
					endLoop = true;
					break;
				}
				
				if (bit != 2 && image[i][j] == 2)
					image[i][j] = bit;

				if (bit == 0)
					zeros++;
				else if (bit == 1)
					ones++;
				else if (bit == 2)
					twos++;
			}
		}

		if (endLoop)
		{
			break;
		}

		if (zeros < minZeros)
		{
			minZeros = zeros;
			result = ones * twos;
		}
	}

	printf("Result: %d\n", result);

	for (int i = 0; i < ROWS; i++)
	{
		for (int j = 0; j < COLS; j++)
			if (image[i][j] == 2)
				printf("\033[30;m ");
			else if (image[i][j] == 1)
				printf("\033[30;47m ");
			else
				printf("\033[37;40m ");
		putchar('\n');
	}

	printf("\033[30;m");
}
