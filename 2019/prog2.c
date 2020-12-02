#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int main(void)
{
	int origArr[4096];
	int size = 0;
	while (scanf("%d,", &origArr[size]) == 1) size++;

	int arr[size];
	int noun = 0, verb = 0;
	origArr[1] = noun;
	origArr[2] = verb;
	for (;;)
	{
		int pos = 0;
		for (int i = 0; i < size; i++)
			arr[i] = origArr[i];
		for (;;)
		{
			if (arr[pos] == 1)
			{
				arr[arr[pos + 3]] = arr[arr[pos + 1]] + arr[arr[pos + 2]];
			}
			else if (arr[pos] == 2)
			{
				arr[arr[pos + 3]] = arr[arr[pos + 1]] * arr[arr[pos + 2]];
			}
			else if (arr[pos] == 99)
			{
				break;
			}
			pos += 4;
		}

		if (arr[0] == 19690720)
			break;

		noun++;
		if (noun == 100)
		{
			noun = 0;
			verb++;
		}

		origArr[1] = noun;
		origArr[2] = verb;
	}
	
	printf("Noun = %d, Verb = %d, Answer = %d\n", noun, verb, 100 * noun + verb);
}
