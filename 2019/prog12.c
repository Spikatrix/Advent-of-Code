#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define NO_OF_MOONS 4  // Already know this, that's why I hash defined it
#define NO_OF_STEPS 1000

struct point3
{
	int x, y, z;
};

struct moonData
{
	struct point3 position;
	struct point3 velocity;

	int energy;
};

struct h
{
	struct moonData data[NO_OF_MOONS];
};

void getMoonInputs    (struct moonData []);
void addToHistory     (struct h**, unsigned int*, struct moonData []);
void updateMoonData   (struct moonData []);
bool alreadyInHistory (struct h*,  unsigned int, struct moonData[]);
void printMoonData    (struct moonData []);

int main(void)
{
	struct moonData moon[NO_OF_MOONS];
	struct h* history = NULL;
	unsigned int historySize = 0;

	getMoonInputs(moon);
	addToHistory(&history, &historySize, moon);
	printMoonData(moon);

	unsigned int steps = 0;
	for (;;)
	{
		updateMoonData(moon);
		addToHistory(&history, &historySize, moon);
		if (alreadyInHistory(history, historySize, moon))
		{
			break;
		}
		steps++;
	}

	printMoonData(moon);
	printf("Steps: %u\n", steps);

	free(history);
}

void getMoonInputs(struct moonData moon[])
{
	for (int i = 0; i < NO_OF_MOONS; i++)
	{
		scanf(" <x=%d, y=%d, z=%d>", &moon[i].position.x, &moon[i].position.y, &moon[i].position.z);
		moon[i].velocity.x = moon[i].velocity.y = moon[i].velocity.z = moon[i].energy = 0;
	}
}

void updateMoonData(struct moonData moon[])
{
	for (int i = 0; i < NO_OF_MOONS - 1; i++)
	{
		for (int j = i + 1; j < NO_OF_MOONS; j++)
		{
			int offset = -(moon[i].position.x > moon[j].position.x) + (moon[i].position.x < moon[j].position.x);
			moon[i].velocity.x += offset;
			moon[j].velocity.x -= offset;
			
			offset = -(moon[i].position.y > moon[j].position.y) + (moon[i].position.y < moon[j].position.y);
			moon[i].velocity.y += offset;
			moon[j].velocity.y -= offset;

			offset = -(moon[i].position.z > moon[j].position.z) + (moon[i].position.z < moon[j].position.z);
			moon[i].velocity.z += offset;
			moon[j].velocity.z -= offset;
		}
	}

	for (int i = 0; i < NO_OF_MOONS; i++)
	{
		moon[i].position.x += moon[i].velocity.x;
		moon[i].position.y += moon[i].velocity.y;
		moon[i].position.z += moon[i].velocity.z;

		moon[i].energy = (abs(moon[i].position.x) + abs(moon[i].position.y) + abs(moon[i].position.z)) *
			(abs(moon[i].velocity.x) + abs(moon[i].velocity.y) + abs(moon[i].velocity.z));
	}
}

void addToHistory(struct h** history, unsigned int* historySize, struct moonData moon[])
{
	*history = realloc(*history, (*historySize + 1) * sizeof **history);
	for (int i = 0; i < NO_OF_MOONS; i++)
	{
		(*history)[*historySize].data[i].position.x = moon[i].position.x;
		(*history)[*historySize].data[i].position.y = moon[i].position.y;
		(*history)[*historySize].data[i].position.z = moon[i].position.z;
		(*history)[*historySize].data[i].velocity.x = moon[i].velocity.x;
		(*history)[*historySize].data[i].velocity.y = moon[i].velocity.y;
		(*history)[*historySize].data[i].velocity.z = moon[i].velocity.z;
	}
	(*historySize)++;
}

bool alreadyInHistory(struct h* history, unsigned int historySize, struct moonData moon[])
{
	for (unsigned int i = 0; i < historySize - 1; i++)
	{
		bool sameData = true;
		for (int j = 0; j < NO_OF_MOONS; j++)
		{
			if (history[i].data[j].position.x != moon[j].position.x ||
				history[i].data[j].position.y != moon[j].position.y ||
				history[i].data[j].position.z != moon[j].position.z ||
				history[i].data[j].velocity.x != moon[j].velocity.x ||
				history[i].data[j].velocity.y != moon[j].velocity.y ||
				history[i].data[j].velocity.z != moon[j].velocity.z)
			{
				sameData = false;
				break;
			}
		}

		if (sameData == true)
		{
			puts("Gotcha!");
			return true;
		}
	}

	return false;
}
void printMoonData(struct moonData moon[])
{
	int totalEnergy = 0;
	for (int i = 0; i < NO_OF_MOONS; i++)
	{
		printf("Pos = %4d %4d %4d \t Velocity = %4d %4d %4d \t Energy = %4d\n",
			moon[i].position.x, moon[i].position.y, moon[i].position.z,
			moon[i].velocity.x, moon[i].velocity.y, moon[i].velocity.z,
			moon[i].energy);

		totalEnergy += moon[i].energy;
	}
	printf("Total energy = %d\n", totalEnergy);
}

