#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *neo, *first, *past;
	unsigned int i = 0;

	if (head == NULL)
		return (0);
	neo = malloc(sizeof(listint_t));
	if (neo == NULL)
	{free(neo);
		return (NULL);}
	if (*head == NULL)
	{neo->n = number;
		neo->next = NULL;
		*head = neo;
		return (neo);}
	first = *head;
	neo->n = number;
	for (; neo->n > first->n && first != NULL; past = first,
		     first = first->next, i++)
	{
		if (first->next == NULL)
			break;}
	if (first->next != NULL)
	{
		if (i != 0)
		{
			past->next = neo;
			neo->next = first;}
		else
		{
			neo->next = *head;
			*head = neo;
		}
	}
	else
	{
		first->next = neo;
		neo->next = NULL;
	}
	return (neo);
}
