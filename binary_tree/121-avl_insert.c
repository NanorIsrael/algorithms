#include "binary_trees.h"

// int max_(int a,int b)
// {
//  	return (a>b)?a:b;
// }

// int height(avl_t *node)
// {
// 	if(node==NULL)
// 		return 0;

//  	return node->height;
// }

// int Balance(avl_t *node)
// {
// 	if(node==NULL)
// 		return 0;

//  	return height(node->left) - height(node->right);
// }

// avl_t *LeftRotate(avl_t *z)
// {
// 	avl_t *y = z->right;
// 	avl_t *t2 = y->left;

// 	y->left = z;
// 	z->right = t2;

// 	z->height = max(height(z->left),height(z->right))+1;
// 	y->height = max(height(y->left),height(y->right))+1;

// 	if (t2 != NULL)
//         t2->parent = z;

// 	y->parent = z->parent;
//     z->parent = y;

// 	return y;
// }

// avl_t *RightRotate(avl_t *z)
// {
// 	avl_t *y = z->left;
// 	avl_t *t3 = y->right;

// 	y->right = z;
// 	z->left = t3;

// 	z->height = max(height(z->left),height(z->right))+1;
// 	y->height = max(height(y->left),height(y->right))+1;
// 	if (t3 != NULL)
//         t3->parent = z;

// 	y->parent = z->parent;
//     z->parent = y;

// 	return y;
// }


// avl_t *FindMin(avl_t *node)
// {
// 	while(node->left!=NULL)
// 		node = node->left;

// 	return node;
// }

// avl_t *Delete(avl_t *root,int data)
// {
// 	if(root==NULL)
// 		return root;

// 	if(data < root->n)
// 		root->left = Delete(root->left,data);

// 	else if(data > root->n)
// 		root->right = Delete(root->right,data);

// 	else
// 	{
// 		if(root->right==NULL && root->left==NULL)
// 		{
// 			free(root);
// 			root = NULL;
// 		}

// 		else if(root->left!=NULL && root->right==NULL)
// 		{
// 			avl_t *temp = root->left;
// 			root = root->left;
// 			free(temp);
// 		}

// 		else if(root->right!=NULL && root->left==NULL)
// 		{
// 			avl_t *temp = root->right;
// 			root = root->right;
// 			free(temp);
// 		}

// 		else
// 		{
// 			avl_t *temp = FindMin(root->right);
// 			root->n = temp->n;
// 			root->right = Delete(root->right,temp->n);
// 		}
// 	}
// 	if(root==NULL)
// 		return root;

// 	root->height = 1 + max(height(root->left),height(root->right));

// 	int balance = Balance(root);

// 	//Left Left Case
// 	if(balance > 1 && Balance(root->left) >=0)
// 		return RightRotate(root);

// 	// Right Right Case
// 	if(balance < -1 && Balance(root->right) <=0)
// 		return LeftRotate(root);

// 	// Left Right Case
// 	if(balance > 1 && Balance(root->left) < 0)
// 	{
// 		root->left = LeftRotate(root->left);
// 		return RightRotate(root);
// 	}
	
// 	//Right Left Case
// 	if(balance < -1 && Balance(root->right) > 0)
// 	{
// 		root->right = RightRotate(root->right);
// 		return LeftRotate(root);
// 	}
// 	return root;
// }

// avl_t *avl_insert(avl_t **tree, int data)
// {
// 	avl_t * new_node = NULL;

//     if (tree == NULL)
//         return NULL;

//     if (*tree == NULL)
//     {
//         *tree = binary_tree_node(NULL, data);
//         return *tree;
//     }

//     if (data < (*tree)->n)
//     {
// 		 new_node = avl_insert(&((*tree)->left), data);
// 		(*tree)->left = new_node;
//     }
//     else if (data > (*tree)->n)
//     {
// 		new_node = avl_insert(&((*tree)->right), data);
// 		(*tree)->right = new_node;
//     }
//     else
//     {
//         // Duplicate values are not allowed in an AVL tree
//         return NULL;
//     }

//     // Update height
//     (*tree)->height = max(height((*tree)->left), height((*tree)->right)) + 1;

//     int balance = Balance(*tree);

//     // Left Left Case
//     if (balance > 1 && data < (*tree)->left->n)
//         return RightRotate(*tree);

//     // Right Right Case
//     if (balance < -1 && data > (*tree)->right->n)
//         return LeftRotate(*tree);

//     // Left Right Case
//     if (balance > 1 && data > (*tree)->left->n)
//     {
//         (*tree)->left = LeftRotate((*tree)->left);
//         return RightRotate(*tree);
//     }

//     // Right Left Case
//     if (balance < -1 && data < (*tree)->right->n)
//     {
//         (*tree)->right = RightRotate((*tree)->right);
//         return LeftRotate(*tree);
//     }

//     return *tree;
// }





// /**
//  * height - Builds a Binary Search Tree from an array
//  *
//  * @node: Pointer to the first element of the array to be converted
//  * Return: Pointer to the root node of the created BST, or NULL on failure
//  */
// int height(avl_t *node)
// {
// 	if (node == NULL)
// 		return (0);

// 	return (node->height);
// }
// /**
//  * balance - Builds a Binary Search Tree from an array
//  *
//  * @node: Pointer to the first element of the array to be converted
//  *
//  * Return: Pointer to the root node of the created BST, or NULL on failure
//  */
// int balance(avl_t *node)
// {
// 	if (node == NULL)
// 		return (0);

// 	return (height(node->left) - height(node->right));
// }


// /**
//  * avl_insert - Builds a Binary Search Tree from an array
//  *
//  * @tree: Pointer to the first element of the array to be converted
//  * @data: data to insert
//  * Return: Pointer to the root node of the created BST, or NULL on failure
//  */
// avl_t *avl_insert(avl_t **tree, int data)
// {
// 	int bal;
// 	avl_t *new_node = NULL;

// 	if (tree == NULL)
// 		return (NULL);
// 	if (*tree == NULL)
// 	{
// 		*tree = binary_tree_node(NULL, data);
// 		return (*tree);
// 	}
// 	if (data < (*tree)->n)
// 	{
// 		new_node = avl_insert(&((*tree)->left), data);
// 		(*tree)->left = new_node;
// 	}
// 	else if (data > (*tree)->n)
// 	{
// 		new_node = avl_insert(&((*tree)->right), data);
// 		(*tree)->right = new_node;
// 	}
// 	else
// 		return (NULL);
// 	(*tree)->height = max_(height((*tree)->left), height((*tree)->right)) + 1;
// 	bal = balance(*tree);
// 	if (bal > 1 && data < (*tree)->left->n)
// 		return (binary_tree_rotate_right(*tree));
// 	if (bal < -1 && data > (*tree)->right->n)
// 		return (binary_tree_rotate_left(*tree));
// 	if (bal > 1 && data > (*tree)->left->n)
// 	{
// 		(*tree)->left = binary_tree_rotate_left((*tree)->left);
// 		return (binary_tree_rotate_right(*tree));
// 	}
// 	if (bal < -1 && data < (*tree)->right->n)
// 	{
// 		(*tree)->right = binary_tree_rotate_right((*tree)->right);
// 		return (binary_tree_rotate_left(*tree));
// 	}
// 	return (*tree);
// }

#include "binary_trees.h"
#include <limits.h>
#include <math.h>

void avl_balancer(avl_t **tree, int val);

/**
 * insert_helper - insert a node in AVL tree
 * @tree: AVL tree
 * @parent: node parent
 * @node: double pointer to the new node
 * @val: the value of the new node
 * Return: NULL (failed) | node/tree (success)
 */
avl_t *insert_helper(avl_t **tree, avl_t *parent, avl_t **node, int val)
{
	if (*tree == NULL)
	{
		*node = binary_tree_node(parent, val);
		return (*node);
	}
	if ((*tree)->n > val)
	{
		(*tree)->left = insert_helper(&(*tree)->left, *tree, node, val);
		if ((*tree)->left == NULL)
			return (NULL);
	}
	else if ((*tree)->n < val)
	{
		(*tree)->right = insert_helper(&(*tree)->right, *tree, node, val);
		if ((*tree)->right == NULL)
			return (NULL);
	}
	else
		return (*tree);

	avl_balancer(tree, val);
	return (*tree);
}

/**
 * avl_balancer - balance the AVL tree
 * @tree: AVL tree
 * @val: value of the node to insert
 */
void avl_balancer(avl_t **tree, int val)
{
	int isBalanced;

	isBalanced = binary_tree_balance(*tree);
	if (isBalanced > 1 && (*tree)->left->n > val)
		*tree = binary_tree_rotate_right(*tree);

	else if (isBalanced > 1 && (*tree)->left->n < val)
	{
		(*tree)->left = binary_tree_rotate_left((*tree)->left);
		*tree = binary_tree_rotate_right(*tree);
	}
	else if (isBalanced < -1 && (*tree)->right->n < val)
		*tree = binary_tree_rotate_left(*tree);
	else if (isBalanced < -1 && (*tree)->right->n > val)
	{
		(*tree)->right = binary_tree_rotate_right((*tree)->right);
		*tree = binary_tree_rotate_left(*tree);
	}
}

/**
 * avl_insert - insert a new node in an AVL
 * @tree: tree
 * @val: val of the new node
 * Return: node (success) | NULL (failed)
 */
avl_t *avl_insert(avl_t **tree, int val)
{
	bst_t *node = NULL;

	if ((*tree) == NULL)
	{
		(*tree) = binary_tree_node(*tree, val);
		return (*tree);
	}

	insert_helper(tree, *tree, &node, val);
	return (node);
}
