"""
Linked list implementation in Python using primitive data types
"""


class Node:
    """
    A Class to create nodes of a linked list
    data: The data to be inserted in the linked list
    next: Pointer to the next node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A class for Linked Lists
    head: Always points to the first node at index 0
    """
    def __init__(self):
        """
        Linked List object constructor
        """
        self.head = None

    def print_list(self):
        """

        Returns
        -------
        Return Nodes in Linked List
        """
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        """

        Parameters
        ----------
        data: Data to be inserted in a Linked List

        Returns
        -------
        Appends the data after the last node
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """

        Parameters
        ----------
        data: Data to be inserted in the Linked List

        Returns
        -------
        Inserts the data at index=0 and changes the head of the linked list to new node inserted
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert_after_node(prev_node, data):
        """

        Parameters
        ----------
        prev_node: Node after which the new Node to be inserted
        data: Data to be inserted in the new Node

        Returns
        -------
        Inserts the data at the given position
        """
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """

        Parameters
        ----------
        key: The Data of the Node that needs to be deleted

        Returns
        -------
        Delete the Node containing Key as data, else return "Key not found"
        """
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        """

        Parameters
        ----------
        pos: Position of the Node that needs to be deleted

        Returns
        -------
        Delete the Node at the given position. If the position==0
        move the Head to the next node and delete
        """
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        """

        Returns
        -------
        Iterate through the Linked list and return length of the linked list
        """
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        """

        Parameters
        ----------
        node: Nodes of the Linked List

        Returns
        -------
        While the Node is not Null, that is not reached end of the list
        continue counting the length of the Linked List
        """
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
