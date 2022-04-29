# Stack and Queue 

## Challenge

Create a Stack and a Queue class that utilizes Nodes to initialize.

## Approach & Efficiency

Using a proactive testing approach build Queues and Lists We have designed tests ahead of the build before completion in order to rid any bugs before they happen.

Big O Time - O(1) regardless of how long either structure gets it will take the same amount of time to remove and add values.
Big O Space - O(1) The space will only ever increase by one and when you do any operation it will only ever affect one item. 

## API

### Stack

|Method|What does it do?|
:---:|:---|
|push | Puts new nodes onto the stack|
|pop | Remove items from stack.| 
|peek | When you peek you will view the value of the top Node in the stack.|
|is_empty|checks if stack is empty and returns a boolean value|

### Queue

|Method|What does it do?|
:---:|:---|
|enqueue | Puts new nodes into the queue|
|dequeue | Remove items from stack front of the queue.| 
|peek | When you peek you will view the value of the front Node in the queue.|
|is_empty|checks if queue is empty and returns a boolean value|