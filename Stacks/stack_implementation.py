"""
Implementation of Stack in Python using Lists
"""
class Stack:
    """
    A class used to represent Stack

    ...

    Attributes
    ----------
    item : any
        the elements that needs to be pushed to stack
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
    def __init__(self):
        """
        Stack Constructor
        """
        self.items = []
    def push(self,item):
        """
        Function to push elements to stack
        Parameters:
            item: An items that user wants to insert into the stack
        Returns:
            None
        """
        self.items.append(item)
    def pop(self):
        """
        Function to pop element at Top(Peak)
        Parameters:
            None
        Returns:
            None
        """
        return self.items.pop()
    def is_empty(self):
        """
        Function to check if the stack is empty
        Parameters:
            None
        Returns:
            True if stack is empty else False
        """
        return self.items == []
    def peak(self):
        """
        Functions to get the element at Top/Peak
        Parameters:
            None
        Returns:
            Item at Peak/Top
        """
        if self.is_empty():
            return "Stack is Empty"
        return self.items[-1]
    def get_stack(self):
        """
        Function to get all the elements in Stack
        Parameters:
            None
        Returns:
            All elements in Stack
        """
        return self.items