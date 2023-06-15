#include "lists.h"


size_t dlistint_len(const dlistint_t *h)
{
    const dlistint_t *current = h;
    int num_node = 0;

    if (current == NULL)
    {
      return 0;
    }
    while (current != NULL)
    {
        num_node += 1;
        current = current->next;
    }

    return num_node;
}
