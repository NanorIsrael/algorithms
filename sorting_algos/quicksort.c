#include <stdio.h>
#include <stdlib.h>

void print_array(int *array, size_t size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int *merge(int *left, int *right, int left_size, int right_size) {
    int *mergedList = malloc((left_size + right_size) * sizeof(int));

    int i = 0, j = 0, k = 0;

    while (i < left_size && j < right_size) {
        if (left[i] <= right[j]) {
            mergedList[k] = left[i];
            i++;
        } else {
            mergedList[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < left_size) {
        mergedList[k] = left[i];
        i++;
        k++;
    }
    while (j < right_size) {
        mergedList[k] = right[j];
        j++;
        k++;
    }

    return mergedList;
}

void quick_sort(int *array, int start, int end) {
    if (start >= end) {
        return;
    }

    int pivot = array[start];
    int *less_than_pivot;
    int *greater_than_pivot;
    int lesthancounter = 0;
    int greater_counter = 0;

    greater_than_pivot = malloc((end - start) * sizeof(int));
    less_than_pivot = malloc((end - start) * sizeof(int));

    for (int i = start + 1; i <= end; i++) {
        if (pivot < array[i]) {
            greater_than_pivot[greater_counter] = array[i];
            greater_counter++;
        } else {
            less_than_pivot[lesthancounter] = array[i];
            lesthancounter++;
        }
    }

    quick_sort(less_than_pivot, 0, lesthancounter - 1);
    quick_sort(greater_than_pivot, 0, greater_counter - 1);

    int *mergedList = merge(less_than_pivot, greater_than_pivot, lesthancounter, greater_counter);

    // Copy the merged list back to the original array
    for (int i = 0; i < lesthancounter; i++) {
        array[start + i] = mergedList[i];
    }
    array[start + lesthancounter] = pivot;
    for (int i = 0; i < greater_counter; i++) {
        array[start + lesthancounter + 1 + i] = mergedList[lesthancounter + i];
    }

    free(less_than_pivot);
    free(greater_than_pivot);
    free(mergedList);
}

int main() {
    int arr[] = {5, 2, 7, 4, 1, 8, 3, 6};
    size_t size = sizeof(arr) / sizeof(arr[0]);

    printf("Original Array: ");
    print_array(arr, size);

    quick_sort(arr, 0, size - 1);

    printf("Sorted Array: ");
    print_array(arr, size);

    return 0;
}
