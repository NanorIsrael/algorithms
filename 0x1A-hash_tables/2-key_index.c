#include "hash_tables.h"

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
    if (size == 0 || strlen((const char *)key) == 0)
        return (0);

    unsigned long int hash = hash_djb2(key);
    unsigned long int index = hash % size;

    return (index);
}



// int main(void)
// {
//     char *s;
//     unsigned long int hash_table_array_size;

//     hash_table_array_size = 1024;
//     s = "cisfun";
//     printf("%lu\n", hash_djb2((unsigned char *)s));
//     printf("%lu\n", key_index((unsigned char *)s, hash_table_array_size));
//     s = "Don't forget to tweet today";
//     printf("%lu\n", hash_djb2((unsigned char *)s));
//     printf("%lu\n", key_index((unsigned char *)s, hash_table_array_size));
//     s = "98";
//     printf("%lu\n", hash_djb2((unsigned char *)s));
//     printf("%lu\n", key_index((unsigned char *)s, hash_table_array_size));  
//     return (EXIT_SUCCESS);
// }