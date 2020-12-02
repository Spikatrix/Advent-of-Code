#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
	char parent[1024][4] = {0};
	char child[1024][4] = {0};
	char temp[1024][4] = {0};

	int orbitIndex = 0;
	char startOrbit[4];
	int startIndex;
	int steps = 0;
	while (scanf(" %[^)])%s", parent[orbitIndex], child[orbitIndex]) == 2)
	{
		if (strcmp(child[orbitIndex], "YOU") == 0)
		{
			strcpy(startOrbit, parent[orbitIndex]);
			startIndex = orbitIndex;
		}

		orbitIndex++;
	}

	int tempIndex = 0;
	strcpy(temp[tempIndex++], startOrbit);
	int tempIndices[1024];
	tempIndices[0] = startIndex;

	bool found = false;

	for (;;)
	{
		int repeat = tempIndex;
		do 
		{
			char searchStr[4];
			int index = tempIndices[tempIndex - 1];
			strcpy(searchStr, temp[--tempIndex]);

			for (int j = 0; j < orbitIndex; j++)
			{
				if (j == index || j == startIndex)
					continue;
	
				if (strcmp(searchStr, child[j]) == 0)
				{
					if (strcmp(parent[j], "SAN") == 0)
					{
						found = true;
						break;
					}
					if (tempIndex > 0)
					{
						strcpy(temp[tempIndex], temp[tempIndex - 1]);
						tempIndices[tempIndex] = tempIndices[tempIndex - 1];
						tempIndices[tempIndex - 1] = j;
						strcpy(temp[tempIndex - 1], parent[j]);
					}
					else
					{
						tempIndices[tempIndex] = j;
						strcpy(temp[tempIndex], parent[j]);
					}
					tempIndex++;
				}
				else if (strcmp(searchStr, parent[j]) == 0)
				{
					if (strcmp(child[j], "SAN") == 0)
					{
						found = true;
						break;
					}
					if (tempIndex > 0)
					{
						strcpy(temp[tempIndex], temp[tempIndex - 1]);
						tempIndices[tempIndex] = tempIndices[tempIndex - 1];
						tempIndices[tempIndex - 1] = j;
						strcpy(temp[tempIndex - 1], child[j]);
					}
					else
					{
						tempIndices[tempIndex] = j;
						strcpy(temp[tempIndex], child[j]);
					}
					tempIndex++;
				}
				else
				{
					continue;
				}

			}
			repeat--;
		} while (!found && repeat > 0);

		if (found)
			break;
		else
			steps++;
	}

	printf("Steps: %d\n", steps);
}
