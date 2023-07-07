#include "hash_tables.h"

char *hash_table_get(const hash_table_t *ht, const char *key)
{

    if (ht == NULL || strlen(key) == 0)
        return (NULL);
    
    // unsigned long index = key_index((const unsigned char *)strdup(key), ht->size);
    // hash_node_t *current_item = ht->array[index];
    
    // if (current_item == NULL)
    //         return (NULL);
    // else
    // {
    //     if (current_item->next != NULL)
    //     {
    //         return NULL;
    //     }
    // }
    return NULL;
}


int main(void)
{
    hash_table_t *ht;
    char *value;

    ht = hash_table_create(1024);
    hash_table_set(ht, "c", "fun");
    hash_table_set(ht, "python", "awesome");
    hash_table_set(ht, "Bob", "and Kris love asm");
    hash_table_set(ht, "N", "queens");
    hash_table_set(ht, "Asterix", "Obelix");
    hash_table_set(ht, "Betty", "Cool");
    hash_table_set(ht, "98", "Battery Street");
    hash_table_set(ht, "c", "isfun");

    // value = hash_table_get(ht, "python");
    // printf("%s:%s\n", "python", value);
    // value = hash_table_get(ht, "Bob");
    // printf("%s:%s\n", "Bob", value);
    // value = hash_table_get(ht, "N");
    // printf("%s:%s\n", "N", value);
    // value = hash_table_get(ht, "Asterix");
    // printf("%s:%s\n", "Asterix", value);
    // value = hash_table_get(ht, "Betty");
    // printf("%s:%s\n", "Betty", value);
    // value = hash_table_get(ht, "98");
    // printf("%s:%s\n", "98", value);
    // value = hash_table_get(ht, "c");
    // printf("%s:%s\n", "c", value);
    // value = hash_table_get(ht, "javascript");
    // printf("%s:%s\n", "javascript", value);


      print_ht(ht);
    free(ht->array);
    free(ht);
    return (EXIT_SUCCESS);
}