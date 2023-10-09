#include "search_algos.h"


int binary_search(int *array, size_t size, int value)
{
	size_t i=0, first_idx=0, last_idx = size - 1, mid ;

	if (array == NULL || size == 0)
	{
		return (-1);
	}

	while (first_idx <= last_idx)
	{
		mid = first_idx + (last_idx - first_idx)/ 2;
        printf("Searching in array: ");
        for (i=first_idx; i <= last_idx; i++) {
            printf("%d", array[i]);
            if (i < last_idx) {
                printf(", ");
            }
        }
		printf("\n");
		if (array[mid] == value)
		{
			printf("\n");
			return (mid);
		}
		else if (array[mid] < value)
		{
			first_idx = mid + 1;
		}
		else
		{		
			last_idx = mid - 1;
		}
	}
	
	return (-1);
}
