class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        '''
        Add item to queue
        '''
        if self.top is None:
            self.top = Node(value)
        else:
            self.top.next = self.top
            self.top = Node(value)
        

    def pop(self):
        '''
        Remove and return first item from queue
        '''
        if self.top is None:
            raise InvalidOperationError 
        temp = self.top.value
        self.top = self.top.next
        return temp

    def peek(self):
        '''
        Check what is the value of first item
        '''
        if not self.top:
            raise InvalidOperationError
        else:   
            return self.top.value

    def is_empty(self):
        '''
        Check if queue is empty
        '''
        if self.top is None:
            return True
        else:
            return False
class Node:
    """
    Node for stack
    """
    def __init__(self, data=None, next_=None):
        self.value = data
        self.next = next_


class InvalidOperationError(Exception):
    """
    Custom Exception
    """
    pass