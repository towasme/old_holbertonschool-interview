#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * binary_tree_node - creates a binary tree node
 * @parent: pointer to the parent node of the node to create
 * @value: value to put in the new node
 *
 * Return: a pointer to the new node or NULL on failure
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *bin;

	bin = malloc(sizeof(binary_tree_t));
	if (!bin)
	{
		return (NULL);
	}

	bin->n = value;
	bin->parent = parent;
	bin->left = NULL;
	bin->right = NULL;
	return (bin);
}
