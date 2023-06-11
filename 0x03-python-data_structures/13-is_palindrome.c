#include "lists.h"
#include <stdlib.h>
/**
 * *reverse_listint - reverse linked list
 * @head: head
 * Return: new reverse linked list
 */
listint_t *reverse_listint(listint_t *head)
{
	const listint_t *current = head;
	listint_t *new_list = NULL;

	while (current)
	{
		listint_t *new_node = malloc(sizeof(listint_t));

		if (!new_node)
			return (NULL);
		new_node->n = current->n;
		new_node->next = new_list;
		new_list = new_node;
		current = current->next;
	}
	return (new_list);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *lst_rev = reverse_listint(*head);

	while ((*head) && lst_rev)
	{
		if ((*head)->n != lst_rev->n)
			return (0);
		(*head) = (*head)->next;
		lst_rev = lst_rev->next;
	}
	return (1);
}

