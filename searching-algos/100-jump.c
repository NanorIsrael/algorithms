#include "search_algos.h"
#include <math.h>

int jump_search(int *array, size_t size, int value)
{
	size_t step = (int)sqrt(size);
	int prev = 0, i;

	while (array[prev] < value)
	{
		int cur = fmin(prev + step, size - 1);
		printf("Value checked array[%d] = [%d]\n", prev, prev);

		if (array[cur] >= value) 
		{
			printf("Value found between indexes [%d] and [%d]\n", prev, cur);
			for (i=prev; i<=cur; i++)
			{
				printf("Value checked array[%d] = [%d]\n", i, i);
				if (array[i] == value)
				{
					return (i);
				}
			}
			return (-1);
		}
		

		prev = cur;
		if (prev >= (int)size - 1)
		{
			return (-1);
		}
	}
	return (-1);
}
