#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

int permutations[212][5];
int permIndex = 0;

void swap(int* a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

void permute(int *arr, int l, int r)
{
	if (l == r)
	{
		for (int i = 0; i < 5; i++)
		{
			permutations[permIndex][i] = arr[i];
			printf("%d ", arr[i]);
		}
		putchar('\n');
		permIndex++;
	}
	else
	{
		for (int i = l; i < r; i++)
		{
			swap(arr + l, arr + i);
			permute(arr, l + 1, r);
			swap(arr + l, arr + i);
		}
	}
}

int main(void)
{
	long int arr[4096];
	long int size = 0;
	while (scanf("%ld,", &arr[size]) == 1) size++;

	permute((int[]) {5, 6, 7, 8, 9}, 0, 5);
	long int maxOutput = 0;

	//int arr[size];

	for (int p = 0; p < permIndex; p++)
	{
			long int output = 0;
			long int prevInput = 0;
			bool done = false, firstRun = false;
			for (int m = 0; !done; m = (m + 1) % 5)
			{
					bool secondInput = false;
					// Code for p1
					//for (int i = 0; i < size; i++)
					//		arr[i] = origArr[i]; 

					int pos = 0;
					long a, b, c;
					for (;;)
					{
							a = b = c = 0;

							int opcode;
							if (arr[pos] >= 100)
							{
									long temp = arr[pos];

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

							long arg1, arg2;
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
									if (secondInput || !firstRun)
									{
											secondInput = false;
											arr[arr[pos + 1]] = prevInput;
											if (m == 4)
												firstRun = false;
									}
									else
									{
											arr[arr[pos + 1]] = permutations[p][m];
											secondInput = true;
									}
									pos += 2;
							}
							else if (opcode == 4)
							{
									printf("Output = %ld\n", arr[arr[pos + 1]]);
									output = arr[arr[pos + 1]];
									prevInput = arr[arr[pos + 1]];
									pos += 2;
									if (output < -10000000000000000 || output > 10000000000000) break;
								
						//			if (firstRun)
						//				break;
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
									printf("%d done\n", m);
									if (!firstRun)
									{
										done = true;
									}
									pos++;
									break;
							}
					}
			}
			puts("---------");
			if (maxOutput < output)
				maxOutput = output;
		}
		printf("Max output = %ld\n", maxOutput);
}
