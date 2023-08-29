#include "binary_trees.h"

void binary_tree_delete(binary_tree_t *tree)
{
    if (tree == NULL)
    {
        return;
    }

    // Delete the left subtree
    binary_tree_delete(tree->left);

    // Delete the right subtree
    binary_tree_delete(tree->right);

    // Delete the current node
    free(tree);
}
