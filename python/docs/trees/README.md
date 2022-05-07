# Trees


## Challenge
<!-- Description of the challenge -->

## Approach & Efficiency

Testing approach was done pre-emptively creating tests before writing the program to make sure that everything worked as expected out of the gate.

Effiency:
Space: O1 as you are always just adding one item to the tree each time.
Time: O(n) as the tree gets bigger it'll take more time to traverse in order to put the node where it needs to go. 

## API

Node - Item with a value in tree
Root  - the base node


Depth Traversal -

Pre-order: Traversal happens  root >> Left >> right

In-Order: Traversal happens left >> root >> right

Post-order: Traversal happens left >> right >> root

Searching -

Contains: Will iterate over the tree to detect if a value is contained. 