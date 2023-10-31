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
	}
	if (current->next == NULL)
	{
		if (current->n > newNode->n)
		{
			newNode->next = current;
			current->next = NULL;
			*head = newNode;
		}
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
		}
		current = current->next;
	}
	return (head);
}
