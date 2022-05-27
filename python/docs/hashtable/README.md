# Hashtables

## Challenge

Create a Hash Table Data Structure with set, get, keys, contains, hash.

## Approach & Efficiency

Built using TDD to verify as it was built well from the ground up.

Efficiency:

Generally this procedure will take an O(1) Time and space complexity if everything goes well, however... Due to the instantiation of a linked list to handle collisions.

TIME O(n) - Due to the use of a linked list to handle collisions at worse you'l hit a collision and have the key prviously in the list and have to itterate over the linked list to find it or realize it doesn't exist and add it.

Space O(n) - The larger the hash table the more space it takes, not only that but as you add key,value pairs you may have collisions and use a linked list making things take more space as you add more information.

## API

`set()`
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
`get()`
        Arguments: key
        Returns: Value associated with that key in the table
`contains()`
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
`keys()`
        Returns: Collection of keys
`hash()`
        Arguments: key
        Returns: Index in the collection for that key
