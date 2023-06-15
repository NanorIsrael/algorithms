#include "lists.h"

/**
 * sum_dlistint - get the sum of all the data `n` of a `dlistint_t` LL
 * @head: head of doubly LL
 * Return: sum of all `n` or 0 if LL is empty
 */
int sum_dlistint(dlistint_t *head)
{
    dlistint_t *current = head;
    int sum = 0;
    
    if (current == NULL)
    {
        return 0;
    }

    while (current != NULL)
    {
        sum += current->n;
        current = current->next;
    }

    return sum;
}
