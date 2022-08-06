"""
Stack ADT implementation using NumPY
"""
import numpy as np


class Stack:
    """
    A class used to represent Stack

    ...

    Attributes
    ----------
    count: The counter to check number of elements in the NumPY Array
    capacity: The total allowed size of NumPY Array
    my_arr: Numpy Arry
    Methods
    -------
    __init__ : self
        Object constructor of class Stack
    push(item):
        accepts the element that needs to be pushed and pushes to stack through top
    pop():
        pop the element at Top
    is_empty:
        check if there are elements in stack. If stack is empty return True
    peak:
        check for the last element in the stack and returns the element
    get_stack:
        return all the elements in the stack
    """
    def __init__(self, capacity):
        """

        Parameters
        ----------
        capacity: The total allowed size of the NumPY Array
        """
        self.count = 0
        self.capacity = capacity
        self.top = -1
        self.my_arr = np.empty(capacity, 'i')

    def push(self, item):
        """

        Parameters
        ----------
        item: Item to be pushed to stack

        Returns
        -------
        None : If Stack is not full and inserts element
        "Stack is full" otherwise
        """
        try:
            if self.top == -1:
                self.count = self.top
                self.my_arr[self.top] = item
                self.top = self.top - 1

            else:
                self.my_arr[self.top] = self.my_arr[self.top+1]
                self.my_arr[-1] = item
                self.count = self.top

        except IndexError:
            print("Stack is full")

    def pop(self):
        """

        Returns
        -------
        None: Pushes the element at the top index
        """
        try:
            last, self.my_arr = self.my_arr[-1], self.my_arr[:-1]
            return last
        except IndexError:
            return "Stack is Empty"

    def is_empty(self):
        """

        Returns
        -------
        Status of the stack(Empty/Full)
        """
        if self.my_arr.size == 0:
            return True
        return False

    def peak(self):
        """
        Returns
        -------
        Element at the top index
        """
        if self.is_empty():
            return "Stack is empty"
        return self.my_arr[-1]

    def get_stack(self):
        """

        Returns
        -------
        Prints the stack to console
        """
        return self.my_arr[self.count:]


exmp = Stack(2)
exmp.push(3)
print(exmp.get_stack())
print('Peak after first push:', exmp.peak())
exmp.push(4)
print(exmp.get_stack())
print('Peak after second push:', exmp.peak())
print(exmp.pop())
print(exmp.get_stack())
print('Peak after first pop:', exmp.peak())
print(exmp.pop())
print(exmp.get_stack())
print('Peak after second pop:', exmp.peak())
print(exmp.pop())
