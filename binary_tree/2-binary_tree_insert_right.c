#include "binary_trees.h"


binary_tree_t *binary_tree_insert_right(binary_tree_t *parent, int value)
{
    if (parent == NULL)
    {
        return NULL;
    }

    binary_tree_t *newRight = binary_tree_node(parent, value); // Create new left node
    if (newRight == NULL)
    {
        return NULL;
    }

    newRight->right = parent->right; // Set new node's left child
    parent->right = newRight; // Update parent's left pointer

    return newRight;
}
