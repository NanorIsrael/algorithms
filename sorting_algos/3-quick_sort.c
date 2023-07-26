#include <stdio.h>
#include <stdlib.h>
#include "sort.h"

void swap(int *array, int i, int j) {
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

int partition(int *array, int low, int high) {
    int pivot = array[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (array[j] < pivot) {
            i++;
            swap(array, i, j);
        }
    }

    swap(array, i + 1, high);
    print_array(array, high + i - );

    return i + 1;
}

void quick_sort(int *array, int low, int high) 
{

    if (low < high) {
        int pi = partition(array, low, high);
        quick_sort(array, low, pi - 1);
        quick_sort(array, pi + 1, high);
    }

}


int main() {
    int array[] = {19, 48, 99, 71, 13, 52, 96, 73, 86, 7};
    int size = sizeof(array) / sizeof(array[0]);

    printf("Original Array: ");
    print_array(array, size);

    quick_sort(array, 0, size - 1);

    printf("Sorted Array: ");
    print_array(array, size);

    return 0;
}
