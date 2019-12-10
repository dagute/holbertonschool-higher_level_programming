#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the list to verify
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *verify, *tmp;

	verify = list;
	tmp = list;

	if (tmp && verify && verify->next)
	{
		verify = verify->next->next;
		tmp = tmp->next;
		while (verify == tmp)
			return (1);
	}
	return (0);
}
