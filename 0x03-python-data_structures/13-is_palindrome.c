#include "lists.h"
#include <stddef.h>
listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *tm, *rv, *md;
	size_t size = 0, a;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tm = *head;
	while (tm)
	{
		size++;
		tm = tm->next;
	}
	tm = *head;
	for (a = 0; a < (size / 2) - 1; a++)
		tm = tm->next;
	if ((size % 2) == 0 && tm->n != tm->next->n)
		return (0);
	tm = tm->next->next;
	rv = reverse_listint(&tm);
	md = rv;

	tm = *head;
	while (rv)
	{
		if (tm->n != rv->n)
			return (0);
		tm = tm->next;
		rv = rv->next;
	}
	reverse_listint(&md);
	return (1);
}
