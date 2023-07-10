#include "hash_tables.h"

/**
 * hash_table_delete - delete given hash table
 * @ht: hash table given
 */
void hash_table_delete(hash_table_t *ht)
{
    unsigned long int idx = 0;
    unsigned long int count = 0;
    
    if (ht == NULL)
        return;
      
    for (; idx < ht->size; idx++)
    {
        free(ht->array[idx]);
        ht->array[idx] = NULL;
    }

    free(ht->array);
    ht->array[idx] = NULL;
    free(ht);
}


// /**
//  * main - check the code
//  *
//  * Return: Always EXIT_SUCCESS.
//  */
// int main(void)
// {
//     hash_table_t *ht;
//     char *key;
//     char *value;

//     ht = hash_table_create(1024);
//     hash_table_set(ht, "c", "fun");
//     hash_table_set(ht, "python", "awesome");
//     hash_table_set(ht, "Bob", "and Kris love asm");
//     hash_table_set(ht, "N", "queens");
//     hash_table_set(ht, "Asterix", "Obelix");
//     hash_table_set(ht, "Betty", "Cool");
//     hash_table_set(ht, "98", "Battery Streetz");
//     key = strdup("Tim");
//     value = strdup("Britton");
//     hash_table_set(ht, key, value);
//     key[0] = '\0';
//     value[0] = '\0';
//     free(key);
//     free(value);
//     hash_table_set(ht, "98", "Battery Street"); 

//     hash_table_set(ht, "hetairas", "Bob");
//     hash_table_set(ht, "hetairas", "Bob Z");
//     hash_table_set(ht, "mentioner", "Bob");
//     hash_table_set(ht, "hetairas", "Bob Z Chu");
//     hash_table_print(ht);
//     hash_table_delete(ht);
//     return (EXIT_SUCCESS);
// }