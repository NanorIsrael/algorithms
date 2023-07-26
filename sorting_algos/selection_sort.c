#include <stdio.h>
#include <stdlib.h>
// #include "sort.h"
void swap(int a, int b)
{
    int temp;

    temp = a;
    a = b;
    b = temp;
}
// int *selection_sort(int *myarray, int size);
// int *bubble_sort(int *myarray, int size);
// int *insertion_sort(int *myarray, int size);
// int *merge_sort(int *myarray, int size);
// int *split(int *myarray, int start, int end);
// int *merge(int *left, int *right, int mid, int size);
void print_array(const int *array, size_t size);
void selection_sort(int *array, size_t size);

int main()
{
    unsigned long int idx;
    // int myarray[] = {9, 5, 6, 7, 1, 8, 2, 4, 3};
    int myarray[] = {19, 48, 99, 71, 13, 52, 96, 73, 86, 7};

    int size = sizeof(myarray) / sizeof(myarray[0]);

    // int *array  =
     selection_sort(myarray, size);
    // int *array  = bubble_sort(myarray, size);
    // int *array = insertion_sort(myarray, size);
    // int *array = merge_sort(myarray, size);


    // for (idx = 0; idx < size; idx++)
    // {
    //     printf("%d\n", array[idx]);
    // }
}






// void selection_sort(int *myarray, int size)
// {
//     unsigned long int idx;
//     int temp;

//     if (a)

//     for (int i = 0; i < size - 1; i++)
//     {

//         for (idx = i + 1; idx < size; idx++)
//         {

//             if (myarray[idx] < myarray[i])
//             {
//                 temp = myarray[i];
//                 myarray[i] = myarray[idx];
//                 myarray[idx] = temp;
//                 print_array(array, size);
//             }
//         }
        
//     }
// }
// void selection_sort(int *array, size_t size)
// {
//     size_t i, j, temp, min_index;

//     for (i = 0; i < size - 1; i++)
//     {
//         min_index = i;
//         for (j = i + 1; j < size; j++)
//         {
//             if (array[j] < array[min_index])
//             {
//                 min_index = j;
//             }
//         }

//         if (min_index != i)
//         {
//             temp = array[i];
//             array[i] = array[min_index];
//             array[min_index] = temp;
//             print_array(array, size);
//         }
//     }
// }
/**
 * selection_sort - Sorts an array of integers in ascending order
 *                  using the selection sort algorithm.
 * @array: An array of integers.
 * @size: The size of the array.
 *
 * Description: Prints the array after each swap.
 */
void selection_sort(int *array, size_t size)
{
    size_t i, j, temp, min_value = 0;

    while (i < size - 1)
    {
        min_value = i;
        j = i + 1;
        while (j < size)
        {
            if (array[j] < array[min_value])
            {
                min_value = j;
            }
            j++;
        }
        if (min_value != i)
        {
                temp = array[i];
                array[i] = array[min_value];
                array[min_value] = temp;
                print_array(array, size);
        }
        i++;
    }
}
// int *bubble_sort(int *myarray, int size)
// {
//     unsigned long int idx;
//     int temp, sorted = 1; 

    
//     for (int i = 0; i < size - 1; i++)
//     {
//         for (idx = 0; idx < size - i - 1; idx++)
//         {
//             if (myarray[idx] > myarray[idx + 1])
//             {
//                 temp = myarray[idx];
//                 myarray[idx] = myarray[idx + 1];
//                 myarray[idx + 1] = temp;
//             }
//         }
//     }

//     return myarray;
// }

// int *merge_sort(int *myarray, int size)
// {
    
//     int idx;
//     int mid = size / 2;

//     if (size <= 1)
//     {
//         return myarray;
//     }
//     int *left_half = split(myarray, 0, mid);
//     int *right_half = split(myarray, mid , size);

//     int *left = merge_sort(left_half, mid);
//     int *right = merge_sort(right_half, size - mid);
    
//     free(left_half);
//     free(right_half);
   
//     return merge(left, right, mid, size);
// }
// int *merge(int *left, int *right, int mid, int size)
// {
//     int i = 0;
//     int j = 0;

//     int *mergedList = malloc(size * sizeof(int));

//     while (i < mid && j < (size - mid))
//     {
//         if (left[i] < right[j]) 
//         {
//             mergedList[i + j] = left[i];
//             i++;    
//         }
//         else
//         {
//             mergedList[i + j] = right[j];   
//             j++;        
//         }  
//     }
//     while (i < mid)
//     {
//         mergedList[i + j] = left[i];
//         i++;
//     }
//     while (j < mid)
//     {
//         mergedList[i + j] = right[j];
//         j++;
//     }
//     return mergedList;
// }
// int *split(int *myarray, int start, int end)
// {
//     int *newArray = malloc(sizeof(int) * (end -start));

//     for (int idx=0; idx < (end - start); idx++)
//     {
//         newArray[idx] = myarray[start + idx];
//     }

//     return newArray;
// }

// int *insertion_sort(int *myarray, int size)
// {
//     unsigned long int idx;
//     int temp, key, swaped = 0; 

    
//     for (int i = 1; i < size; i++)
//     {
//         key = myarray[i];
//         idx = i - 1;
      
//         while (idx >= 0 && myarray[idx] > key)
//         {
//             myarray[idx + 1] = myarray[idx];
//             idx -= 1;
//         }
//         myarray[idx + 1] = key;
//     }

//     return myarray;
// }

void print_array(const int *array, size_t size)
{
    size_t i;

    i = 0;
    while (array && i < size)
    {
        if (i > 0)
            printf(", ");
        printf("%d", array[i]);
        ++i;
    }
    printf("\n");
}