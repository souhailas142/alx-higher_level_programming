#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list, *s = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (f == s)
			return (1);
	}
	return (0);
}
