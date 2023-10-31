#include "lists.h"
/**
 * inser_node - Insert new node to sorted linked list
 * @head: listint_t
 * @number: int
 * Return: listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	if (current == NULL)
	{
		*head = newNode;
		return (*head);
	}
	if (current->next == NULL)
	{
		if (current->n > newNode->n)
		{
			newNode->next = current;
			current->next = curreny->next;
			*head = newNode;
		}
		else
			current->next = newNode;
		return (*head);
	}
	if (current->n > newNode->n)
	{
		newNode->next = current;
		current->next = curren->next;
		*head = newNode;
		return (*head);
	}
	while (current->next != NULL)
	{
		if ((current->next)->n > newNode->n)
		{
			newNode->next = current->next;
			current->next = newNode;
			break;
		}
		if (current->next == NULL)
		{
			current->next = newNode;
			break;
		}
		current = current->next;
	}
	return (*head);
}
