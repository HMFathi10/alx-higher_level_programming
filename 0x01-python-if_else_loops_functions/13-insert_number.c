#include "lists.h"
/**
 * inser_node - Insert new node to sorted linked list
 * @head: listint_t
 * @number: int
 * Return: listint_t
 */
listint_t *insert_node(listint_t **head, int number);
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
	while (current != NULL)
	{
		if (current->next > newNode->n)

	}
	return (1);
}
