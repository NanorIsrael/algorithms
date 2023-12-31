#include "binary_trees.h"

/**
 * array_to_bst - Builds a Binary Search Tree from an array
 *
 * @array: Pointer to the first element of the array to be converted
 * @size: Number of elements in the array
 *
 * Return: Pointer to the root node of the created BST, or NULL on failure
 */
bst_t *bst_search(const bst_t *tree, int value)
{
    if (tree == NULL)
        return NULL;

		if (value == tree->n)
			return ((bst_t *)tree);

        if (value < tree->n)
        {
			return bst_search(tree->left, value);
        }
		else
		{
			return bst_search(tree->right, value);
		}
		
}
