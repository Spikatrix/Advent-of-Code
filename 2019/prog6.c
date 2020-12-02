#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int main(void)
{
	char parent[1024][4];
	char child [1024][4];

	int orbitIndex = 0;
	int startIndex;
	while (scanf(" %[^)])%s", parent[orbitIndex], child[orbitIndex]) == 2)
	{
		if (strcmp(child[orbitIndex], "YOU") == 0)
		{
			startIndex = orbitIndex;
		}

		orbitIndex++;
	}

	char stack[1024][4];
	int skipIndex[1024];
	int stackPointer = -1;

	strcpy(stack[++stackPointer], parent[orbitIndex]);
	skipIndex[stackPointer - 1] = orbitIndex;

	int steps = 0;
	for (bool found = false; !found;)
	{
		int repeat = stackPointer;
		int currentPointer = stackPointer;

		char searchOrbit[4];
		strcpy(searchOrbit, stack[stackPointer--]);

		do
		{
			for (int i = 0; i < orbitIndex; i++)
			{
				if (skipIndex[currentPointer] == i)
					continue;

				if (strcmp(searchOrbit, child[i]) == 0)
				{
					for (int j = 0; j < currentPointer; j++)
					{
						strcpy(stack[currentPointer + j + repeat], stack[currentPointer + j]);
					}
					strcpy(stack[++stackPointer], parent[j]);
					// TODO: Assign something here? hmm
				}
			}
			repeat--;
		} while (repeat > 0);
	}

	printf("Steps = %d\n", steps);
}
