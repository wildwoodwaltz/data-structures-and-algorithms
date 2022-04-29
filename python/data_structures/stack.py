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
        node = Node(value)
        node.next = self.top
        self.top = node
        

    def pop(self):
        '''
        Remove and return first item from queue
        '''
        try: 
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        '''
        Check what is the value of first item
        '''
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
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
   