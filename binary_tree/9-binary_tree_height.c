#include "binary_trees.h"

size_t binary_tree_height(const binary_tree_t *tree)
{
	size_t left_height = 0;
	size_t right_height = 0;

	if (tree == NULL)
		return (0);
	else
	{

		left_height = binary_tree_height(tree->left);
		right_height = binary_tree_height(tree->right);


		if (tree->left && tree->left->parent != NULL)
		{
				left_height += 1;
		}
		if (tree->right && tree->right->parent != NULL)
		{
				right_height += 1;
		}
		
		if (left_height > right_height )
			return left_height;
		else
			return right_height;
	}
}
