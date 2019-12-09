#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *a = list, *b = list;

	while (a != NULL && b != NULL && a->next != NULL)
	{
		a = a->next->next;
		b = b->next;
		if (a == b)
			return(1);
	}
	return (0);
}
