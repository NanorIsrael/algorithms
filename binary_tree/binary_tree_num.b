 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>

 typedef struct Node {
	int data;
	struct Node *left;
	struct Node *right;
 } binaryNode;

binaryNode *createBinaryNode(int leftKey);
 binaryNode *insert(binaryNode *root, int Key);
void inorderTraversal(binaryNode *root, char *position);

int main(void)
 {
	binaryNode *root;

	root = createBinaryNode(21);
	insert(root, 8);
	 insert(root, 2);
	

	insert(root, 5);
	insert(root,3);
	insert(root, 7);
		insert(root, 4);


	inorderTraversal(root, "root");

	return (0);
 }

 binaryNode *createBinaryNode(int key) {
	binaryNode *root;

	root = malloc(sizeof(binaryNode));
	root->data = key;
	root->left = NULL;
	root->right = NULL;

	return root;
 }

binaryNode *insert(binaryNode *root, int value)
{
	if (root == NULL)
		return createBinaryNode(value);
	if (value < root->data)
		root->left = insert(root->left, value);
	else
		root->right = insert(root->right, value);

	return root;
}

void inorderTraversal(binaryNode *root, char *position)
{
	binaryNode *current;

	if (root != NULL)
	{
		printf("on %s \n", position);
		inorderTraversal(root->left, "left of root");
		printf("%d \n", root->data);
		inorderTraversal(root->right, "right of root");
		// current = root->left;
		// printf("left branch:\n");
		// while (current != NULL)
		// {

		// 	printf("%d\n", current->data);
		// 	current = current->left;
		// }
		// current = root->right;
		// printf("right branch:\n");
		// while (current != NULL)
		// {

		// 	printf("%d\n", current->data);
		// 	current = current->right;
		// }
	}
}