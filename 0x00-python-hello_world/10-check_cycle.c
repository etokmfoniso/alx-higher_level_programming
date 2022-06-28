i#include "lists.h"

/**
 * check_cycle - checks if a linked list contains
 * @list: linked list to check
 *
 * Return: 1 if the list was a cycle, 0 if it isnt 
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = lists;
	listint_t *fast = lists;

	if (!list)
		return (0);

	while (slow && fast && fast ->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
