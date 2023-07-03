#!/usr/bin/python3
"""Defines a class square"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.__data = value
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data
        
    @data.setter
    def data(self, value):
        if not isinstance(value, int) and value is not None:
            raise TypeError("next_node must be a integer")
        self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node
        
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current is not None and value >= current.data:
                current = current.next_node
            new_node.next_node = current
            current = new_node


    def __str__(self):
        tmp = self.__head;
        new_list = []
        while tmp is not None:
            new_list.append(str(tmp.data))
            tmp = tmp.next_node
        return('\n'.join(new_list))

sll = SinglyLinkedList()
sll.sorted_insert(9)
sll.sorted_insert(1)
sll.sorted_insert(5)
sll.sorted_insert(2)
sll.sorted_insert(7)
sll.sorted_insert(3)
print(sll)