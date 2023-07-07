#include "hash_tables.h"


int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
    
    if (ht == NULL || strlen(key) == 0 || strlen(value) == 0)
        return (0);

    hash_node_t *item = malloc(sizeof(hash_node_t *));
    item->key = malloc(sizeof(char *) * strlen(key) + 1);
    item->value = malloc(sizeof(char *) * strlen(value) + 1);

    if (item == NULL || item->key == NULL || item->value == NULL)
        return (0);
    
    item->key = (char *)key;
    strcpy(item->value, strdup(value));

    unsigned long index = key_index((const unsigned char *)strdup(key), ht->size);
    hash_node_t *current_item = ht->array[index];

    if (current_item == NULL)
    {
        // check if table is not full here
        ht->array[index] = item;
        ht->array[index]->next = NULL;
    }
    else
    {
        // handle collision here
        while (current_item->next != NULL)
        {
            current_item->next = current_item->next->next;
        }
        item->next = current_item->next;
        ht->array[index]->next = item;
        // item = current_item;
    }

    return (1);
}

void print_ht(hash_table_t *ht)
{
    unsigned long int idx = 0;

    printf("\nHash Table\n-------------------\n");
    for (; idx < ht->size; idx++)
    {
        if (ht->array[idx])
        {
            hash_node_t * current = ht->array[idx];

            printf("index: %lu: key: %s -> value: %s\n",  idx, current->key, current->value);

            while (current->next != NULL)
            {
                if (current->next->key != NULL && current->next->value != NULL)
                {
                    printf("index: %lu: key: %s -> value: %s\n",  idx, current->next->key, current->next->value);
                }
                current->next = current->next->next;
            }
        }
    }
}


// int main(void)
// {

//     hash_table_t *ht;

//      ht = hash_table_create(1024);
//     hash_table_set(ht, "c", "fun");
//     hash_table_set(ht, "python", "awesome");
//     hash_table_set(ht, "Bob", "and Kris love asm");
//     hash_table_set(ht, "N", "queens");
//     hash_table_set(ht, "Asterix", "Obelix");
//     hash_table_set(ht, "Betty", "Cool");
//     hash_table_set(ht, "98", "Battery Street");
//     hash_table_set(ht, "c", "isfun");

// //     ht = hash_table_create(1024);
//     hash_table_set(ht, "betty", "cool");
//     hash_table_set(ht, "betty", "cool");
//     // hetairas collides with mentioner
//     hash_table_set(ht, "hetairasdwe", "val 1");
//     hash_table_set(ht, "hetairas", "val 2");
//     hash_table_set(ht, "mentioner", "val 3");
//     hash_table_set(ht, "heliotropes", "val 4");
//     hash_table_set(ht, "neurospora", "val 4");
//     hash_table_set(ht, "depravement", "val 5");
//     hash_table_set(ht, "serafins", "val 6");
//     hash_table_set(ht, "stylist", "val 7");
//     hash_table_set(ht, "subgenera", "val 7");
//     hash_table_set(ht, "joyful", "val 7");
//     hash_table_set(ht, "synaphea", "val 8");
//     hash_table_set(ht, "synaphea", "val 8");
//     print_ht(ht);
//     free(ht->array);
//     free(ht);
//     return (EXIT_SUCCESS);
// }