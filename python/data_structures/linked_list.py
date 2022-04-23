class LinkedList:
    """
    This module allows us to create a linked list by creating nodes and adding them to the beginning of the linked list, all while setting thier value. It is singly linked and only goes one direction. 
    """

    def __init__(self):
        self.head = None
        self.list = []

    def __str__(self):
        string = ""
        if self.head == None:
            return 'NULL'
        current = self.head
        while current:
            string += f"{ {current.value} } -> "
            current = current.next
        string += 'NULL'
        return string.replace("'", " ")
         

    def insert(self, data=None):   
        self.head = Node(data, self.head)
        
    def includes(self, query):
        #method body here
        current = self.head
        while current:
            if current.value == query:
                return True
            current=current.next
        return False

class Node:
    def __init__(self, data=None, next_=None):
        self.value = data
        self.next = next_


class TargetError:
    pass
