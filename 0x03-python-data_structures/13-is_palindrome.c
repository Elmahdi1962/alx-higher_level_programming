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
	listint_t *tmp_head = *head;
	int list_len = 0, *list_numbers, i = 0;

	if (*head == NULL || head == NULL)
		return (1);
	/* count how many nodes the list have */
	while (tmp_head != NULL)
	{
		list_len++;
		tmp_head = tmp_head->next;
	}
	/* if the list has one node it's counted as palindrome */
	if (list_len == 1)
		return (1);
	/* create an array to hold the numbers in each node */
	list_numbers = malloc(sizeof(int) * list_len);
	if (list_numbers == NULL)
		return (0);
	tmp_head = *head;
	/* loop thru the list again and assign each*/
	/* node's number to the array we created */
	while (tmp_head != NULL)
	{
		list_numbers[i] = tmp_head->n;
		tmp_head = tmp_head->next;
		i++;
	}
	/* loop thru the array of numbers to half + 1 */
	/* and compare it to it's opposite index */
	for (i = 0; i < (list_len + 1) / 2; i++)
	{
		if (list_numbers[i] != list_numbers[(list_len - 1) - i])
		{
			free(list_numbers);
			return (0);
		}
	}
	free(list_numbers);
	return (1);
}
