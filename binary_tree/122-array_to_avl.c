#include "binary_trees.h"

avl_t *array_to_avl(int *array, size_t size)
{
    bst_t *root = NULL;
    size_t i;

    if (array == NULL || size == 0)
        return NULL;

    for (i = 0; i < size; i++)
    {
        if (avl_insert(&root, array[i]) == NULL)
        {
            // Ignore if value is already present in the tree
            continue;
        }
    }

    return root;
}
