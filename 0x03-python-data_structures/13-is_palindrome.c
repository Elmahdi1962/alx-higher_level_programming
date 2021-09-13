#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - check is a linked list is palindrome
 * @head: head of the list
 * Return: 0 if not 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *prev, *next, *left_head, *right_head;
	int list_len = 0, i = 0, not_p = 0;

	if (*head == NULL || head == NULL)
		return (1);
	/* count how many nodes the list have */
	while (current != NULL)
	{
		list_len++;
		current = current->next;
	}
	/* if the list has one node it's counted as palindrome */
	if (list_len == 1)
		return (1);
	/* reverse left half */
	current = *head;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		else
		{
			current->next = NULL;
		}
		prev = current;
		current = next;
	}
	/* prev == to head of reversed left half and current == head of right half */
	right_head = current;
	left_head = prev;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		if (list_len % 2 != 0 && i == 1)
			current = current->next;
		if (current->n != prev->n)
		{
			not_p = 1;
			break;
		}
		current = current->next;
		prev = prev->next;
	}
	/* reverse the left half back like it was before */
	current = left_head;
	prev = right_head;
	for (i = 1; i <= list_len / 2 && current != NULL; i++)
	{
		next = current->next;
		if (prev != NULL)
			current->next = prev;
		prev = current;
		current = next;
	}
	if (not_p == 1)
		return (0);
	return (1);
}
