#include "hash_tables.h"

/**
 * hash_table_create - creates a hash table.
 * @size: size of table to create
 * Return: nothing.
 */
hash_table_t *hash_table_create(unsigned long int size)
{
        unsigned long int idx;
        hash_table_t *mytable;

        if (size == 0)
                return (NULL);

        mytable = malloc(sizeof(hash_table_t));
        if (mytable == NULL)
        {
                return (NULL);
        }
        mytable->size = size;

        mytable->array = malloc(sizeof(hash_node_t *) * size);
        if (mytable->array == NULL)
        {
                free(mytable);
                return (NULL);
        }

        for (idx = 0; idx < size; idx++)
                mytable->array[idx] = NULL;

        return (mytable);
}

// int main()
// {
//      hash_table_t *ht;

//     ht = hash_table_create(1024);
//     printf("%p\n", (void *)ht);
//     return (EXIT_SUCCESS);

// }