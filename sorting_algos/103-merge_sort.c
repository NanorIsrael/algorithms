#include "sort.h"
#include <stdlib.h>

int *merge(int *left, int *right, size_t mid, size_t size, int *arr);

int *split(int *arr, int start, int end)
{
    int i;
    int *subarray = malloc((end - start) * sizeof(int));

    for (i = 0; i < (end - start); i++)
    {
        subarray[i] = arr[start + i];
    }
    return subarray;
}

int *merge(int *left, int *right, size_t mid, size_t size, int *arr)
{
    size_t i = 0;
    size_t j = 0;
    // int *mergedList = malloc(size * sizeof(int));

    while (i < mid && j < (size - mid))
    {
        if (left[i] < right[j])
        {
            arr[i + j] = left[i];
            i++;
        }
        else
        {
            arr[i + j] = right[j];
            j++;
        }
    }

    while (i < mid)
    {
        arr[i + j] = left[i];
        i++;
    }
    while (j < (size - mid))
    {
        arr[i + j] = right[j];
        j++;
    }

    return arr;
}

void merge_sort(int *myarray, size_t size)
{
    size_t mid;
    int  *left_half, *right_half;

    if (size <= 1)
    {
        return;
    }

    mid = size / 2;
    left_half = split(myarray, 0, mid);
    right_half = split(myarray, mid, size);

    merge_sort(left_half, mid);
    merge_sort(right_half, size - mid);

    printf("Merging...\n");
    printf("[left]: ");
    print_array(left_half, mid); 
    printf("[right]: ");
    print_array(right_half, size - mid); 
    merge(left_half, right_half, mid, size, myarray);
    printf("[Done]: ");
    print_array(myarray, size); 

    free(left_half);
    free(right_half);
}

