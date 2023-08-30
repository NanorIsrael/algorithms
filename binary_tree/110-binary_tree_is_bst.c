#include "binary_trees.h"

int binary_tree_is_bst_helper(const binary_tree_t *tree, int min, int max);

int binary_tree_is_bst(const binary_tree_t *tree)
{
    if (tree == NULL)
        return (1);

    return binary_tree_is_bst_helper(tree, INT_MIN, INT_MAX);
}

int binary_tree_is_bst_helper(const binary_tree_t *tree, int min, int max)
{
    if (tree == NULL)
        return (1);

    if (tree->n <= min || tree->n >= max)
        return (0);

    return (binary_tree_is_bst_helper(tree->left, min, tree->n) &&
            binary_tree_is_bst_helper(tree->right, tree->n, max));
}
