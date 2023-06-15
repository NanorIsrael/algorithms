#include "lists.h"

/**
 * get_dnodeint_at_index - get the nth node of a `dlistint_t` doubly LL
 * @head: pointer to head of LL
 * @index: node index to return
 * Return: node at index given or NULL if node does not exist
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
    dlistint_t *current = head;
    unsigned int idx = 0;

    if (index == 0 && current != NULL)
    {
        return head;
    }
    else
    {
        while (idx < index && current != NULL)
        {
            if (idx == index - 1)
            {
                return current->next;
            }
            current = current->next;
            idx++;
        }
    }

    return NULL;
}
