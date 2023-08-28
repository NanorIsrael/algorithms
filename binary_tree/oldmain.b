 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>

 typedef struct Node {
	char *text;
	struct Node *left;
	struct Node *right;
 } binaryNode;

binaryNode *createBinaryNode(char *leftKey);
 binaryNode *addRight(binaryNode **root, char *Key);
 binaryNode *addLeft(binaryNode **root, char *Key);
 int main(void) {
	binaryNode *root;
	binaryNode *current;

	root = createBinaryNode("a");
	 addLeft(&root, "b");
	addLeft(&root, "d");
	addLeft(&root, "f");

	// printf("root left %s\n", root->left->text);
	// printf("root left %d\n", root->left->left == NULL);

	addRight(&root, "c");
	addRight(&root, "e");
	addRight(&root, "g");

	printf("root %s\n", root->text);
	current = root->left;

	while (current != NULL)
	{
		printf("root left %s\n", current->text);
	 		// printf("root left %s\n", current->left->text);

		current = current->left;
	}

	current = root->right;

	while (current != NULL)
	{
		printf("root left %s\n", current->text);
	 		// printf("root left %s\n", current->left->text);

		current = current->right;
	}
	
	return (0);
 }

 binaryNode *createBinaryNode(char *key) {
	binaryNode *root;

	root = malloc(sizeof(binaryNode));
	root->text = malloc(sizeof(key) + 1);
	strcpy(root->text, key);
	root->left = NULL;
	root->right = NULL;

	return root;
 }

 binaryNode *addLeft(binaryNode **root, char *leftKey) {
	binaryNode *current = *root;

		while(current->left != NULL)
		{
			current = current->left;
		}
			
		current->left = createBinaryNode(leftKey);
	
	return current;
 }

 binaryNode *addRight(binaryNode **root, char *Key) {
	binaryNode *newRight = *root;

	while(newRight->right != NULL)
		newRight = newRight->right;
	newRight->right = createBinaryNode(Key);

	return newRight;
 }