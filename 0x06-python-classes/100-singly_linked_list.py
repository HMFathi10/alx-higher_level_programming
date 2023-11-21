#!/usr/bin/python3
"""class Node that defines a node of a singly linked list"""


class Node:
    """Represent a square"""

    def __init__(self, data, next_node=None):
        """Initalize Node
        Args:
            data (int): node data
            next_node (Node): next node pointer
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get/Set data"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/Set next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Initalize SinglyLinkedList"""

    def __init__(self):
        """Initalize SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert New node at right position"""
        n = Node(value)
        if self.__head is None:
            n.next_node = None
            self__head = n
        elif self.__head.data > value:
            n.next_node = self.__head
            self.__head = n
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            n.next_node = temp.next_node
            temp.next_node = n

    def __str__(self):
        """Define the print pattern"""
        result = []
        temp = self.__head
        while temp is not None:
            result.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(result))
