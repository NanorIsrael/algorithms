#include "binary_trees.h"


binary_tree_t *binary_tree_insert_left(binary_tree_t *parent, int value)
{
    if (parent == NULL)
    {
        return NULL;
    }

    binary_tree_t *newLeft = binary_tree_node(NULL, value); // Create new left node
    if (newLeft == NULL)
    {
        return NULL;
    }

    newLeft->left = parent->left; // Set new node's left child
    parent->left = newLeft; // Update parent's left pointer

    return newLeft;
}
