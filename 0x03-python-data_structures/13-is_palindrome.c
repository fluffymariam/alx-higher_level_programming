#include "lists.h"
listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev_slow_ptr = *head;
	listint_t *second_half;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	if (fast_ptr != NULL)
		slow_ptr = slow_ptr->next;

	second_half = slow_ptr;
	prev_slow_ptr->next = NULL;
	reverse_list(&second_half);

	is_palindrome = compare_lists(*head, second_half);

	reverse_list(&second_half);
	if (prev_slow_ptr)
		prev_slow_ptr->next = second_half;
	else
		*head = second_half;

	return (is_palindrome);
}

/**
 * reverse_list - Reverses a linked list
 * @head_ref: Pointer to a pointer to the head of the linked list
 */
void reverse_list(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head_ref = prev;
}

/**
 * compare_lists - Compares two linked lists
 * @list1: First linked list
 * @list2: Second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}
