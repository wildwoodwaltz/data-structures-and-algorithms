
def zip_lists(a, b):
    #take three
    current_a = a.head
    current_b = b.head
    if current_a is None or current_b is None:
        if current_b:
            return b
        if current_a:
            return a

    while current_a and current_b:
        if current_a:
            a.insert_after(current_a.value, current_b.value)
            current_a = current_a.next
            current_b = current_b.next
            if current_a.next:
                current_a = current_a.next
        if current_b:
            a.insert_after(current_a.value, current_b.value)
            current_a = current_a.next
            current_b = current_b.next
            if current_a.next:
                current_a = current_a.next
    return a
# Take two 
        # current_a = a.head
        # current_b = b.head

        # while current_b and current_a:
        #     old_next_a = current_a.next
        #     old_next_b = current_b.next

        #     if current_a.next != None:
        #         current_a.next = current_b
        #         current_b.next = old_next_a

        #         current_a = old_next_a
        #         current_b = old_next_b
        #         print(a)
        #     if current_a.next is None:
        #         current_a.next = current_b
        #         while current_b:
        #             a.append(current_b)
        #             current_b = current_b.next
        #     # if current_b.next is              
        # return a




    #     old_next_a = current_b.next
    #     old_next_b = current_a.next
    #     current_a.next = current_b
    #     print(a)
    #     if current_a is not None:
    #         current_b.next = old_next_a
    #         current_a = old_next_a
    #         current_b = old_next_b
    #     print(a)
    # if current_a is None:
    #     if current_b is None:
    #         return a
    #     while current_b:
    #         current_a.next = current_b
    #         current_b = current_b.next
    #         current_a = current_a.next
    # if current_b is None:
    #     while current_a:
    #         current_a = current_a.next