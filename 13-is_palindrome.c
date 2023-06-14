#include "lists.h"

int is_palindrome(listint_t **head){
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *next = NULL;


    int right_end[100];
    int idx = 0, j= 0;

    if (*head == NULL || (*head)->next != NULL)
        return 1;

    while (fast != NULL && fast->next->next != NULL) 
    {
        fast = fast->next->next;
        next = slow->next;
        slow->next = prev;
        prev =  slow;
        slow = next;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    while (slow != NULL) 
    {
        if (prev->n != slow->n)
            return 0;
        
        slow = slow->next;
        prev = prev->next;
    }

    return 1;
}