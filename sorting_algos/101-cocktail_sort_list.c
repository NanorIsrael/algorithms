#include "sort.h"

listint_t *get_list_length(listint_t *h);
int swap_nodes(listint_t **list, listint_t *node);

/**
  * cocktail_sort_list - Sorts a doubly linked list
  * of integers in ascending order using the
  * Cocktail Shaker sort algorithm.
  * @list: The doubly linked list to apply the cocktail sort
  *
  * Return: Nothing!
  */
void cocktail_sort_list(listint_t **list)
{
	listint_t *curr = NULL, *left_limit = NULL, *right_limit = NULL;
	int cycle_type = FORWARD, swapped = 1;

	if (!list || !(*list) || !(*list)->next)
		return;

	curr = *list;
	left_limit = curr;
	right_limit = get_list_length(*list);

    // printf("%p", right_limit);
    do {
        swapped = 0;

        if (left_limit != right_limit)
	    {

            if (curr->n == curr->next->n)
                printf("not called\n");

                // break;
            if (curr->n > curr->next->n && cycle_type == FORWARD)
            {

                swap_nodes(list, curr), print_list(*list);
                swapped=1;
                curr = curr->next;
                void node_forward_pass(listint_t **list, int *swapped, listint_t **start)
            {
                listint_t *curr = *list;
                while (curr != NULL && curr->next != NULL)
                {
                    if (curr->n > curr->next->n)
                    {
                        swap_nodes(list, curr);
                        if (curr->prev == NULL)
                            *start = curr;
                        print_list(*start);
                        *swapped = 1;
                    }
                    else
                    {
                        curr = curr->next;
                    }
                }
                }

            }
            if (curr->next->n < curr->n && cycle_type == BACKWARD)
            {
                                                    printf("not called\n");

                swapped = 1;
                swap_nodes(list, curr), curr = curr->prev, print_list(*list);
                curr = curr->prev;

            }

            if (cycle_type == BACKWARD && curr->next == left_limit)
            {
                cycle_type = FORWARD;
                curr = curr->next;
            }

            if (cycle_type == FORWARD && curr->prev == right_limit)
            {
                right_limit = right_limit->prev;
                cycle_type = BACKWARD;
                curr = curr->prev;
            }
            // swapped =1;
	    }

    } while (swapped);
	
}

/**
  * swap_nodes - Swap two nodes of a doubly linked list
  * @list: The double linked lists that contains the nodes
  * @node: The node to swap with the next node
  *
  * Return: Nothing!
  */
int swap_nodes(listint_t **list, listint_t *node)
{

        node->next->prev = node->prev;

        if (node->next->prev)
            node->prev->next = node->next;
        else
            *list = node->next;

        node->prev = node->next;
        node->next = node->next->next;
        node->prev->next = node;

        if (node->next)
            node->next->prev = node;
        

	return (1);
}

/**
  * get_list_length - Counts the number of elements in a doubly linked list
  * @h: The double linked list to count
  *
  * Return: Number of elements in the doubly linked list
  */
listint_t *get_list_length(listint_t *h)
{
	listint_t *curr = h;
    if (h == NULL)
            return (NULL); 
	while (curr->next != NULL)
		curr = curr->next;

	return (curr);
}