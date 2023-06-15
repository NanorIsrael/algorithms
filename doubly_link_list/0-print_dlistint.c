#include "lists.h"

/**
 * print_dlistint - Print all the values of each node in a `dlistint_t` list
 * @h: head pointer in doubly linked list
 * Return: Number of nodes in LL
 */
size_t print_dlistint(const dlistint_t *h)
{
    const dlistint_t *current = h;
    int num_node = 0;

    if (current == NULL)
    {
      return 0;
    }
    while (current != NULL)
    {
        printf("%d\n", current->n);
        current = current->next;
        num_node += 1;
    }

    return num_node;
}
