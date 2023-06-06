#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head
 * @number: number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *t = *head;
	listint_t *add = NULL;

	add = malloc(sizeof(listint_t));
	if (!add)
		return (NULL);
	add->n = number;
	add->next = NULL;
	while (t)
	{
		if (t->n < number && t->next->n > number)
		{
			add->next = t->next;
			t->next = add;
		}
		t = t->next;
	}
	return (add);
}
