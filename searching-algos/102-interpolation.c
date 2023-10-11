#include "search_algos.h"

/**
 * interpolation_search_recursive - Recursive interpolation search
 * @array: Array to search in
 * @low: Starting index of the subarray
 * @high: Ending index of the subarray
 * @value: Value to search
 * @size: Size of the array
 * Return: Index of the found value or -1 if not found
 */
int interpolation_search_recursive(int *array, int low, int high, int value, size_t size)
{
    if (low <= high && value >= array[low] && value <= array[high])
    {
        int pos = low + ((double)(high - low)
		/ (array[high] - array[low])) * (value - array[low]);

        printf("Value checked array[%d] = [%d]\n", pos, array[pos]);

        if (array[pos] == value)
            return pos;

        if (array[pos] < value)
            return interpolation_search_recursive(array, pos + 1, high, value, size);

        return interpolation_search_recursive(array, low, pos - 1, value, size);
    }

    printf("Value checked array[%d] is out of range\n", low);

    return -1;
}

/**
 * interpolation_search - Initiates interpolation search
 * @array: Array to search in
 * @size: Size of the array
 * @value: Value to search
 * Return: Index of the found value or -1 if not found
 */
int interpolation_search(int *array, size_t size, int value)
{
    if (array == NULL || size == 0)
        return -1;

    return interpolation_search_recursive(array, 0, size - 1, value, size);
}
