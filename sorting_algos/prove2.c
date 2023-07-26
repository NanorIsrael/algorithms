#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
    const int n;
    struct listint_s *prev;
    struct listint_s *next;
} listint_t;
void print_list(listint_t *list)
{
    while (list != NULL)
    {
        printf("%d ", list->n);
        list = list->next;
    }
    printf("\n");
}

listint_t *swapNodes(listint_t *list, listint_t *node1, listint_t *node2)
{
    if (node1 == node2 || node1 == NULL || node2 == NULL)
        return list;

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
    else
        list = node2; // Update the list head if node2 is the new head

    return list;
}


listint_t *cocktailShakerSort(listint_t *list)
{
    if (list == NULL || list->next == NULL)
        return list;

    int swapped;
    listint_t *left = list;
    listint_t *right = NULL;

    do
    {
        swapped = 0;

        // Forward pass
        while (left->next != right)
        {
            if (left->n > left->next->n)
            {
                list = swapNodes(list, left, left->next);
                swapped = 1;
                print_list(list); // Print the list after each pass
            }
            left = left->next;
        }

        if (!swapped)
            break;

        swapped = 0;
        right = left;
        left = left->prev; // Reset left to the last sorted node

        // Backward pass
        while (right->prev != left)
        {
            if (right->n < right->prev->n)
            {
                list = swapNodes(list, right->prev, right);
                swapped = 1;
                print_list(list); // Print the list after each pass
            }
            right = right->prev;
        }
        right = NULL; // Reset right to NULL to restart the forward pass

    } while (swapped);

    return list;
}




int main()
{
    listint_t *list = NULL;
    int array[] = {19, 48, 99, 71, 13, 52, 96, 73, 86, 7};
    size_t n = sizeof(array) / sizeof(array[0]);

    // Create the doubly linked list
    for (int i = n - 1; i >= 0; i--)
    {
        listint_t *newNode = (listint_t *)malloc(sizeof(listint_t));
        if (newNode)
        {
            *((int *)&newNode->n) = array[i];
            newNode->prev = NULL;
            newNode->next = list;
            if (list)
                list->prev = newNode;
            list = newNode;
        }
    }

    printf("Original List: ");
    print_list(list);

    printf("\nSorted List: ");
    list = cocktailShakerSort(list);
    print_list(list);

    return 0;
}
