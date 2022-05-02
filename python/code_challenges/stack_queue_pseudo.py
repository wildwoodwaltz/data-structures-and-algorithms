from data_structures.stack import Stack


class PseudoQueue:
    
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self,value):
        '''
        enqueus items onto inbox stack
        '''
        self.inbox.push(value)


