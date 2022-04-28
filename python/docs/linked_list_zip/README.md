# zip a linked list

Take two linked lists of any length and merge them together zipping one after the next alternating.

## Whiteboard Process -> 

![Whiteboard](./whiteboard.png)

[Final Code](../../code_challenges/linked_list_zip.py)

## Approach & Efficiency

1. Take two lists, a and b
2. start at a.head and insert b.head after
3. set a.head to a.next -> You're on the newly inserted b
4. set b.head to b.next so you can get the new value from the b list.
5. if there is an a.next then advance one more so that you are off the newly added B and back on the next node of the A-list.

c
Big O Space - O(n)? - If function copies list b into A then as list b gets longer it'll take more room. If this actually puts b into a then it's O1. Though I'm sure B is left alone?
Big O Time - O(n) - As the linked list gets longer, it takes more time to finish zipping.