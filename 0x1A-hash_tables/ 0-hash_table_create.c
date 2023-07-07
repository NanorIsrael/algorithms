#include "hash_tables.h"



hash_table_t *hash_table_create(unsigned long int size)
{
    hash_table_t *mytable = malloc(sizeof(hash_table_t *) * size);
    if (mytable == NULL)
    {
        return (NULL);
    }
    mytable->size = size;
    mytable->array = malloc(sizeof(hash_node_t *) * size);
    if (mytable->array == NULL)
    {
        return (NULL);
    }
    return (mytable);
}


// int main()
// {
//      hash_table_t *ht;

//     ht = hash_table_create(1024);
//     printf("%p\n", (void *)ht);
//     return (EXIT_SUCCESS);

// }