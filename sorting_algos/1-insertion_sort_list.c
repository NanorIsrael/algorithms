#include <stdio.h>
#include <stdlib.h>
#include "sort.h"

/**
 * create_listint - Creates a doubly linked list from an array of integers
 *
 * @array: Array to convert to a doubly linked list
 * @size: Size of the array
 *
 * Return: Pointer to the first element of the created list. NULL on failure
 */
listint_t *create_listint(const int *array, size_t size)
{
    listint_t *list;
    listint_t *node;
    int *tmp;

    list = NULL;
    while (size--)
    {
        node = malloc(sizeof(*node));
        if (!node)
            return (NULL);
        tmp = (int *)&node->n;
        *tmp = array[size];
        node->next = list;
        node->prev = NULL;
        list = node;
        if (list->next)
            list->next->prev = list;
    }
    return (list);
}

void insertion_sort_list(listint_t **list){

    
    listint_t * current = *list;
    listint_t * prev, *temp;
    int key;

    while(current != NULL)
    {
        prev = current->prev;
        temp = current;

        while(prev != NULL && prev->n > temp->n) 
        {
            prev->next = temp->next;
            if (temp->next != NULL)
            {
                temp->next->prev = prev;
            }
            temp->next = prev;
            temp->prev = prev->prev;
            prev->prev = temp;
            if (temp->prev != NULL)
            {
                temp->prev->next = temp;
            }
            else
            {
                *list = temp;
            }
            prev = temp->prev;
            print_list(*list);
        }

        current = current->next;
    }
}

