class Queue:
    """
    A list of items that will be retrieved in order of insertion. 
    """

    def __init__(self):
        self.front = None
        self.rear = None
        

    def enqueue(self, value):
        '''
        Add item to queue
        '''
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        else:
            self.rear = Node(value)
            self.front = self.rear
        

    def dequeue(self):
        '''
        Remove and return first item from queue
        '''
        if self.front is None:
            raise InvalidOperationError
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        '''
        Check what is the value of first item
        '''
        if not self.front:
            raise InvalidOperationError
        else:   
            return self.front.value

    def is_empty(self):
        '''
        Check if queue is empty
        '''
        if self.front is None:
            return True
        else:
            return False

class Node:
    """
    Node for queue
    """
    def __init__(self, data=None, next_=None):
        self.value = data
        self.next = next_

class InvalidOperationError(Exception):
    '''
    Custom error Handling
    '''
    pass