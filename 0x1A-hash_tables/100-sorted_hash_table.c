#include "hash_tables.h"

void set_ext(shash_table_t *ht, shash_node_t *hn, shash_node_t *nn, char *key);

/**
* shash_table_create- Creates a sorted hash table.
 * @size: The size of new sorted hash table.
 *
 * Return: If an error occurs - NULL.
 *    Otherwise - a pointer to the new sorted hash table.
 */
shash_table_t *shash_table_create(unsigned long int size)
{
        shash_table_t *ht;
        unsigned long int i;

        ht = malloc(sizeof(shash_table_t));
        if (ht == NULL)
                return (NULL);

        ht->size = size;
        ht->array = malloc(sizeof(shash_node_t *) * size);
        if (ht->array == NULL)
                return (NULL);

        for (i = 0; i < size; i++)
                ht->array[i] = NULL;

        ht->shead = NULL;
        ht->stail = NULL;

        return (ht);
}

int shash_table_set(shash_table_t *ht, const char *key, const char *value)
{
	shash_node_t *new_node, *tmp;
	unsigned long int index;

	if (ht == NULL || key == NULL || *key == '\0' || value == NULL)
		return (0);
	index = key_index((const unsigned char *)key, ht->size);
	tmp = ht->shead;
	while (tmp)
	{
		if (strcmp(tmp->key, key) == 0)
		{
			free(tmp->value);
			tmp->value = strdup(value);
			return (1);
		}
		tmp = tmp->snext;
	}
	new_node = malloc(sizeof(shash_node_t));
	if (new_node == NULL)
		return (0);
	new_node->key = strdup(key);
	new_node->value = strdup(value);
	new_node->next = ht->array[index];
	ht->array[index] = new_node;
        set_ext(ht, ht->shead, new_node, (char *)key);
	return (1);
}
void set_ext(shash_table_t *ht, shash_node_t *hn, shash_node_t *nn, char *key)
{

        shash_node_t  *tmp;

        ht->shead = hn;
	if (ht->shead == NULL)
	{
		nn->sprev = NULL;
		nn->snext = NULL;
		ht->shead = nn;
		ht->stail = nn;
	}
	else if (strcmp(ht->shead->key, key) > 0)
	{
		nn->sprev = NULL;
		nn->snext = ht->shead;
		ht->shead->sprev = nn;
		ht->shead = nn;
	}
	else
	{
		tmp = ht->shead;
		while (tmp->snext != NULL && strcmp(tmp->snext->key, key) < 0)
			tmp = tmp->snext;
		nn->sprev = tmp;
		nn->snext = tmp->snext;
		if (tmp->snext == NULL)
			ht->stail = nn;
		else
			tmp->snext->sprev = nn;
		tmp->snext = nn;
	}
}

/**
 * shash_table_get - Retrieve the value associated with
 *                   a key in a sorted hash table.
 * @ht: A pointer to the sorted hash table.
 * @key: The key to get the value of.
 *
 * Return: If the key cannot be matched - NULL.
 *         Otherwise - the value associated with key in ht.
 */
char *shash_table_get(const shash_table_t *ht, const char *key)
{
        shash_node_t *current;
        unsigned long int index;

        if (ht == NULL || key == NULL || *key == '\0')
                return (NULL);

        index = key_index((const unsigned char *)key, ht->size);
        if (index >= ht->size)
                return (NULL);

        current = ht->shead;
    if (current != NULL)
    {
        while (current != NULL && strcmp(current->key, key) != 0)
                    current = current->snext;

        return (current->value);
    }

        return (NULL);
}

void shash_table_print_rev(const shash_table_t *ht)
{
        shash_node_t *current;

        if (ht == NULL)
                return;

        current = ht->stail;  // Start from the tail
        printf("{");
        while (current != NULL)
        {
                printf("'%s': '%s'", current->key, current->value);
                current = current->sprev;
                if (current != NULL)
                        printf(", ");
        }

        printf("}\n");
}



/**
 *  shash_table_print - Prints a sorted hash table in order.
 * @ht: A pointer to the sorted hash table.
 */
void shash_table_print(const shash_table_t *ht)
{
        shash_node_t *current;

        if (ht == NULL)
                return;


        current = ht->shead;
        printf("{");
        while (current != NULL)
        {
                printf("'%s': '%s'", current->key, current->value);
                current = current->snext;
                if (current != NULL)
                        printf(", ");
        }
        printf("}\n");
}

/**
 * shash_table_delete - Deletes a sorted hash table.
 * @ht: A pointer to the sorted hash table.
 */
void shash_table_delete(shash_table_t *ht)
{
        shash_table_t *head = ht;
        shash_node_t *current, *tmp;

        if (ht == NULL)
                return;

        current = ht->shead;
        while (current)
        {
                tmp = current->snext;
                free(current->key);
                free(current->value);
                free(current);
                current = tmp;
        }

        free(head->array);
        free(head);
}
