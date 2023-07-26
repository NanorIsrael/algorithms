#include <stdio.h>
#include <stdlib.h>

void print_array(int *array, size_t size)
{
    size_t i;
    for (i = 0; i < size; i++)
    {
        printf("%d", array[i]);
        if (i < size - 1)
            printf(", ");
    }
    printf("\n");
}

void bitonic_compare(int *array, size_t size, int dir)
{
    size_t dist = size / 2;
    size_t i;

    for (i = 0; i < dist; i++)
    {
        if ((array[i] > array[i + dist]) == dir)
        {
            int temp = array[i];
            array[i] = array[i + dist];
            array[i + dist] = temp;
        }
    }
}

void bitonic_merge(int *array, size_t size, int dir)
{
    if (size <= 1)
        return;

    size_t dist = size / 2;

    bitonic_compare(array, size, dir);
    bitonic_merge(array, dist, dir);
    bitonic_merge(array + dist, dist, dir);
}

void bitonic_sort_dir(int *array, size_t size, int dir)
{
    if (size <= 1)
        return;

    size_t dist = size / 2;

    printf("Merging [%lu/16] (%s):\n", size, dir == 1 ? "UP" : "DOWN");
    print_array(array, size);
    // Sort the first half in the given direction
    bitonic_sort_dir(array, dist, 1);

    // Sort the second half in the opposite direction
    bitonic_sort_dir(array + dist, dist, 0);

    // Merge both halves in the specified direction
    bitonic_merge(array, size, dir);
    printf("Result [%zu/16] (%s):\n", size, dir == 1 ? "UP" : "DOWN");
    print_array(array, size);

}

void bitonic_sort(int *array, size_t size)
{
   bitonic_sort_dir(array, size, 1);
}

int main()
{
    int array[] = {100, 93, 40, 57, 14, 58, 85, 54, 31, 56, 46, 39, 15, 26, 78, 13};
    size_t size = sizeof(array) / sizeof(array[0]);

    printf("Original Array: ");
    print_array(array, size);

    // Ensure that size is a power of 2 before calling bitonic_sort
    // Otherwise, you may encounter an infinite loop or incorrect results.

    bitonic_sort(array, size);

    printf("Sorted Array: ");
    print_array(array, size);

    return 0;
}
