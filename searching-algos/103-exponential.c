#include "search_algos.h"

int bin_search(int *array, int bound, size_t size, int value);

/**
 * interpolation_search_recursive - Recursive interpolation search
 * @array: Array to search in
 * @low: Starting index of the subarray
 * @high: Ending index of the subarray
 * @value: Value to search
 * @size: Size of the array
 * Return: Index of the found value or -1 if not found
 */
int exponential_search(int *arr, int size, int key)
{
	int bound;

    if (size == 0) {
        return (-1);
    }

    bound = 1;
    while (bound < size && arr[bound] < key) {
		printf("Value checked array[%d] = [%d]\n", bound, arr[bound]);
        bound *= 2;
    }

    return bin_search(arr, bound, size, key);
}

/**
 * linear_search - Performs a linear search for a key value
 * @array: Array to search value
 * @size: size of input array
 * @value: value to search
 * Returns: 1 if found and -1 if not found
 */
int bin_search(int *array, int bound, size_t size, int value)
{
	size_t i = 0, first_idx = bound / 2, mid, last_idx;

	if (array == NULL || size == 0)
	{
		return (-1);
	}

	last_idx = fmin(bound + 1, size) - 1;

	printf("Value found between indexes [%lu] and [%lu]\n", first_idx, last_idx);
	while (first_idx <= last_idx)
	{
		mid = first_idx + (last_idx - first_idx) / 2;
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
