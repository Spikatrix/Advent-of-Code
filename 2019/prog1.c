#include <stdio.h>

int main(void)
{
	unsigned int sum = 0;
	int mass, fuel;
	while (scanf("%d", &mass) == 1) 
	{
		printf("Got mass = %d\n", mass);
		int calc = ((mass / 3) - 2);
		sum += calc;
		fuel = calc;
		for(;;)
		{
			printf("Internal fuel = %d\n", fuel);
			fuel = ((fuel / 3) - 2);
			if (fuel <= 0)
			{
				break;
			}
			sum += fuel;
		}

		printf("Partial fuel = %u\n", sum);
	}
	printf("%u\n", sum);
}
