#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
    int n;
    struct listint_s *prev;
    struct listint_s *next;
} listint_t;

void swapNodes(listint_t **list, listint_t *node1, listint_t *node2)
{
    if (node1 == node2 || node1 == NULL || node2 == NULL)
        return;

    if (node1->prev)
        node1->prev->next = node2;
    if (node2->next)
        node2->next->prev = node1;

    node1->next = node2->next;
    node2->prev = node1->prev;

    node1->prev = node2;
    node2->next = node1;

    if (node1->next)
        node1->next->prev = node1;
    if (node2->prev)
        node2->prev->next = node2;

    if (node1 == *list)
        *list = node2;
    else if (node2 == *list)
        *list = node1;
}

void cocktailSort(listint_t **list)
{
    int swapped = 1;
    listint_t *start = *list;
    listint_t *left = *list;
    listint_t *right = NULL;

    if (*list == NULL || (*list)->next == NULL)
        return;

    while (swapped)
    {
        // Forward pass
        swapped = 0;
        while (left->next != right)
        {
            if (left->n > left->next->n)
            {
                swapNodes(list, left, left->next);
                swapped = 1;
                if (left->prev == NULL)
                    start = left;
            }
            else
            {
                left = left->next;
            }
        }

        // If no swap occurred, the list is sorted
        if (!swapped)
            break;

        // Move the right pointer to the last swapped node
        right = left;

        // Reset the swapped flag for the backward pass
        swapped = 0;

        // Backward pass
        while (right->prev != left)
        {
            if (right->n < right->prev->n)
            {
                swapNodes(list, right->prev, right);
                swapped = 1;
                if (right->prev == NULL)
                    start = right;
            }
            else
            {
                right = right->prev;
            }
        }

        // Move the left pointer to the last swapped node
        left = right;
    }

    // Update the head of the doubly linked list
    *list = start;
}

void printList(listint_t *list)
{
    while (list != NULL)
    {
        printf("%d ", list->n);
        list = list->next;
    }
    printf("\n");
}

listint_t *create_listint(const int *array, size_t size)
{
    listint_t *list = NULL;
    listint_t *node = NULL;

    for (int i = size - 1; i >= 0; i--)
    {
        node = malloc(sizeof(listint_t));
        if (!node)
        {
            // Handle memory allocation failure here if necessary
            return NULL;
        }

        node->n = array[i];
        node->next = list;
        node->prev = NULL;

        if (list)
            list->prev = node;
        list = node;
    }

    return list;
}

int main()
{
    int array[] = {50, 12, 98, 32, 67, 25, 78, 43, 90, 15};
    size_t n = sizeof(array) / sizeof(array[0]);

    listint_t *list = create_listint(array, n);
    if (!list)
    {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Original List: ");
    printList(list);

    cocktailSort(&list);

    printf("Sorted List: ");
    printList(list);

    return 0;
}
