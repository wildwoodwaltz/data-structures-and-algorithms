# Singly Linked List

A singly linked list is a set of `Nodes` with or without a `Value` that connect to each other in one direction. Each Node can only see the node after it, as the reference was made during instantiation of the `node`.  

## Challenge

Create a Node class that has properties for the value of the Node and a pointer to the next Node. Thereby creating a linked list.

## Approach & Efficiency

Using a proactive testing approach to build a Linked list. We have designed tests ahead of the build before completion in order to rid any bugs before they happen.

Big O Time - O(n) as the list gets longer it will take longer to search as you must itterate over each item. 
Big O Space - O(1) When you add an i tem, you only ever add one to the beginning. It will always only add one at a time. 

## API

`insert` - adds a new Node to the beginning of the linked list. 
