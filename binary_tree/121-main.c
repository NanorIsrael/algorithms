#include "binary_trees.h"

/**
 * main - Entry point
 *
 * Return: 0 on success, error code on failure
 */
int main(void)
{
    avl_t *root;
    avl_t *node;
    // printf("Inserted: %d\n", node->n);

    root = NULL;
    node = avl_insert(&root, 98);
    printf("Inserted: %d\n", node->n);
    binary_tree_print(root);
    node = avl_insert(&root, 402);
    printf("\nInserted: %d\n", node->n);
    binary_tree_print(root);
    node = avl_insert(&root, 12);
    printf("\nInserted: %d\n", node->n);
    binary_tree_print(root);
    node = avl_insert(&root, 46);
    printf("\nInserted: %d\n", node->n);
    binary_tree_print(root);
    node = avl_insert(&root, 128);
    printf("\nInserted: %d\n", node->n);
    binary_tree_print(root);
    node = avl_insert(&root, 256);
    printf("\nInserted: %d\n", node->n);
    binary_tree_print(root);
    node = avl_insert(&root, 512);
    printf("\nInserted: %d\n", node->n);
    binary_tree_print(root);
    node = avl_insert(&root, 50);
    printf("\nInserted: %d\n", node->n);
    binary_tree_print(root);
    return (0);
}

void preorder(avl_t *root)
{
	if(root==NULL)
		return;

	printf("%d ",root->n);
	preorder(root->left);
	preorder(root->right);
}

// int main()
// {
// 	avl_t *root = NULL;

// 	avl_insert(&root, 5);
// 	avl_insert(&root,10);
// 	avl_insert(&root,15);
// 	avl_insert(&root,25);
	// root = avl_insert(root,30);
	// root = avl_insert(root,14);
	// root = avl_insert(root,23);
	// root = avl_insert(root,6);
	// root = avl_insert(root,24);
	// root = avl_insert(root,30);
	// root = avl_insert(root,3);

	/*
            BST -->     5
                       /   \
                      3    10
                         /  \
                        6   15
                           /  \
                          14   25
                              /  \
                             23  30
                              \   
                              24   



            AVL TREE -->    15
                          /    \	
                         10     25
                       /   \   /  \
                      5    14 23  30
                    /  \       \
                   3    6      24
	*/

	// printf("\nPreorder traversal of tree is : "); preorder(root);

	// root = Delete(root,10);
	/*	
        After deleting 10
           AVL TREE -->           15
                                /    \	
                               5     25
                             /   \   /  \
                            3    14 23  30
                                /    \
                               6     24
					    
	*/
// 	printf("\nPreorder traversal after deleting 10 is : "); 
// 	preorder(root);

// 	return 0;
// }
