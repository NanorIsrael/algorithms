#include "binary_trees.h"

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
		binary_tree_t *newNode;
		newNode = (binary_tree_t *) malloc(sizeof(binary_tree_t));
		if (newNode == NULL)
		{
			return NULL;
		}

		newNode->n = value;
		newNode->left = NULL;
		newNode->right = NULL;

		if (parent != NULL)
		{
			if (value < parent->n)
				parent->left = newNode;
			else
				parent->right = newNode;
		}

	return newNode;
}
