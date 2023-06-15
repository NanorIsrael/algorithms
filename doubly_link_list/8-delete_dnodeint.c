#include "lists.h"

/**
 * delete_dnodeint_at_index - Delete node at index of a `dlistint_t` LL
 * @head: double pointer to head of LL
 * @index: index position to remove from LL
 * Return: 1 if succeeded, -1 if failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *current = *head;
    unsigned int counter = 0;

    if (index == 0 && current != NULL)
    {

        *head = (*head)->next;
        if (*head != NULL) {
            (*head)->prev = NULL;
        }
        free(current);
        return (1);
    }

    while (current != NULL && counter < index)
    {
        current = current->next;
        counter += 1;
    }

    if (current != NULL) 
    {
        current->prev->next = current->next;
        if (current->next != NULL)
        {
            current->next->prev = current->prev;
        }
        free(current);
        return (1);
    }
     
    return (-1);
}
