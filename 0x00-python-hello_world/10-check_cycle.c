#include "lists.h"
#include <stdlib.h>

/**
 * _realloc - Reallocates a memory block
 * @ptr: The pointer to the previous memory block
 * @old_size: The size of the old memory block
 * @new_size: The size of the new memory block
 *
 * Return: The pointer to the new memory block otherwise NULL
 */
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	void *new_ptr;
	unsigned int min_size = old_size < new_size ? old_size : new_size;
	unsigned int i;

	if (new_size == old_size)
		return (ptr);
	if (ptr != NULL)
	{
		if (new_size == 0)
		{
			free(ptr);
			return (NULL);
		}
		new_ptr = malloc(new_size);
		if (new_ptr != NULL)
		{
			for (i = 0; i < min_size; i++)
				*((char *)new_ptr + i) = *((char *)ptr + i);
			free(ptr);
			return (new_ptr);
		}
		free(ptr);
		return (NULL);
	}
	else
	{
		new_ptr = malloc(new_size);
		return (new_ptr);
	}
}



/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list head
 * Return: 0 if no, 1 if yes
 */

int check_cycle(listint_t *list)
{
	int size = 10, i;
	listint_t *current = list, **nodes = malloc(sizeof(listint_t) * size);

	if (!nodes || !current)
		return (0);

	while (current)
	{
		for (i = 0; nodes[i] != NULL; i++)
		{
			if (current == nodes[i])
				return (1);
		}
		if (i == size || i > size)
		{
			size += 10;
			nodes = _realloc(nodes, sizeof(listint_t) * (size - 10), sizeof(listint_t) * size);
		}
		nodes[i] = current;
		current = current->next;
	}
	return (0);
}
