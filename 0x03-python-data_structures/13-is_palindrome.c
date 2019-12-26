#include "lists.h"
/**
 * is_palindrome - Funtion that checks if a singly linked list is a palindrome
 * @head: Head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, buf[4096];
	listint_t *p;

	if (head == NULL)
		return (0);
	p = *head;
	if (*head == NULL || p->next == NULL)
		return (1);
	for (i = 0; p; p = p->next, i++)
		buf[i] = p->n;
	for (j = 0 , i--; i > j; j++, i--)
	{
		if (buf[j] == buf[i])
		{
			;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
