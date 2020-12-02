#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define INPUT_ID 5

int main(void)
{
	int arr[4096];
	int size = 0;
	while (scanf("%d,", &arr[size]) == 1) size++;

	int pos = 0;
	int a, b, c;
	for (;;)
	{
		a = b = c = 0;

		int opcode;
		if (arr[pos] >= 100)
		{
			int temp = arr[pos];

			opcode = arr[pos] % 10;
			arr[pos] /= 100;
			c = arr[pos] % 10;
			if (arr[pos] > 0)
			{
				arr[pos] /= 10;
				b = arr[pos] % 10;
			}
			if (opcode == 9)
				opcode = 99;

			arr[pos] = temp;
		}
		else
		{
			opcode = arr[pos];
		}

		int arg1, arg2;
		if (c == 0)
			arg1 = arr[arr[pos + 1]];
		else
			arg1 = arr[pos + 1];

		if (b == 0)
			arg2 = arr[arr[pos + 2]];
		else
			arg2 = arr[pos + 2];	

		if (opcode == 1)
		{
			arr[arr[pos + 3]] = arg1 + arg2;
			pos += 4;
		}
		else if (opcode == 2)
		{
			arr[arr[pos + 3]] = arg1 * arg2;
			pos += 4;
		}
		else if (opcode == 3)
		{
			arr[arr[pos + 1]] = INPUT_ID;
			pos += 2;
		}
		else if (opcode == 4)
		{
			printf("Output = %d\n", arr[arr[pos + 1]]);
			pos += 2;
		}
		else if (opcode == 5)
		{
			if (arg1)
			{
				pos = arg2;
			}
			else
			{
				pos += 3;
			}
		}
		else if (opcode == 6)
		{
			if (!arg1)
			{
				pos = arg2;
			}
			else
			{
				pos += 3;
			}
		}
		else if (opcode == 7)
		{
			if (arg1 < arg2)
			{
				arr[arr[pos + 3]] = 1;
			}
			else
			{
				arr[arr[pos + 3]] = 0;
			}
			pos += 4;
		}
		else if (opcode == 8)
		{
			if (arg1 == arg2)
			{
				arr[arr[pos + 3]] = 1;
			}
			else
			{
				arr[arr[pos + 3]] = 0;	
			}
			pos += 4;
		}
		else if (opcode == 99)
		{
			pos++;
			break;
		}
	}
}
