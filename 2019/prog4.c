#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define LOW1 108457
#define HIGH1 562041

#define LOW 197487
#define HIGH 673251

int main(void)
{
	int count = 0;
	bool sameAdj, inc;
	for (int i = LOW; i <= HIGH; i++)
	{
		sameAdj = false;
		inc = true;
		int times = 0;
		char buffer[128];
		sprintf(buffer, "%d", i);
		for (int i = 0, len = strlen(buffer); i < len - 1; i++)
		{
			if (buffer[i] > buffer[i + 1])
			{
				inc = false;
				break;
			}
			if (buffer[i] == buffer[i + 1])
			{
				times++;
			}
			else if (times != 0)
			{
				if (times == 1)
					sameAdj = true;
				else
					times = 0;
			}
		}

		if (times == 1)
			sameAdj = true;

		if (sameAdj && inc)
			count++;
	}

	printf("%d\n", count);
}
