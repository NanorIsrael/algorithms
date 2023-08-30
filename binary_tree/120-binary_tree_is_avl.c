
#include "binary_trees.h"

int max(int a, int b)
{
    return (a > b ? a : b);
}

int height(const binary_tree_t *tree)
{
    if (tree == NULL)
        return -1;

    return 1 + max(height(tree->left), height(tree->right));
}

int binary_tree_balance(const binary_tree_t *tree)
{
    if (tree == NULL)
        return 0;

    return height(tree->left) - height(tree->right);
}

int binary_tree_is_bst_c(const binary_tree_t *tree, int min, int max)
{
    if (tree == NULL)
        return 1;

    if (tree->n <= min || tree->n >= max)
        return 0;

    return binary_tree_is_bst_c(tree->left, min, tree->n) &&
           binary_tree_is_bst_c(tree->right, tree->n, max);
}

int binary_tree_is_avl(const binary_tree_t *tree)
{
    if (tree == NULL)
        return 1;

    int balance = binary_tree_balance(tree);

    if (balance < -1 || balance > 1)
        return 0;

    if (!binary_tree_is_bst_c(tree, INT_MIN, INT_MAX))
        return 0;

    return binary_tree_is_avl(tree->left) && binary_tree_is_avl(tree->right);
}
