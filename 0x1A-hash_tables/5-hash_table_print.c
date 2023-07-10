#include "hash_tables.h"


/**
 * hash_table_print - Print a hash table
 * @ht: hash table
 */
void hash_table_print(const hash_table_t *ht)
{
    unsigned long int idx;
    int count;
    
    printf("{");
    if (ht != NULL)
    {
        for (idx = 0, count = 0; idx < ht->size; idx++)
        {
            hash_node_t *current = ht->array[idx];
            
            if (current != NULL)
            {
                if (count == 1)
                    printf(", ");
                printf("'%s': '%s'", current->key, current->value);

                while (current->next != NULL)
                {
                        printf(", ");
                        printf("'%s': '%s'", current->key, current->value);                   

                        current->next = current->next;
                }
                count = 1;
            }
           
        }
    }
    printf("}\n");
}



int main(void)
{
    hash_table_t *ht;

    ht = hash_table_create(1024);
    hash_table_print(ht);
    hash_table_set(ht, "c", "fun");
    hash_table_set(ht, "python", "awesome");
    hash_table_set(ht, "Bob", "and Kris love asm");
    hash_table_set(ht, "N", "queens");
    hash_table_set(ht, "Asterix", "Obelix");
    hash_table_set(ht, "Betty", "Cool");
    hash_table_set(ht, "98", "Battery Street");
    hash_table_print(ht);
    return (EXIT_SUCCESS);
}