# Stack and Queue Animal Shelter

## Challenge

Create a class called animal shelter which uses a FIFO method for animal adoptions. It takes in one attribute "Animal" and will sort them into either cats or dogs, and then will dequeue by preference.

## Approach & Efficiency

Using a proactive testing approach build Queues and Lists We have designed tests ahead of the build before completion in order to rid any bugs before they happen.

Big O Time - O(1) regardless of how long either structure gets it will take the same amount of time to remove and add values.
Big O Space - O(1) The space will only ever increase by one and when you do any operation it will only ever affect one item. 

## API

Two Queues one for each animal type cats and dogs that we allow. 

### Queue

|Method|What does it do?|
:---:|:---|
|enqueue | Puts new nodes into the queue|
|dequeue | Remove items from stack front of the queue.| 

### Code 

[Final Code](../../code_challenges/stack_queue_animal_shelter.py)

## Whiteboard Process -> 

![Whiteboard](./whiteboard.png)

