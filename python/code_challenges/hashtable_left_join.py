from data_structures.hashtable import Hashtable

def hashmap_left_join(hash_one, hash_two):
    # Establish Hashtable
    hash_a = Hashtable()
    hash_b = Hashtable()
    answer = []
    # Set Hashtable Values (Since given a dict)
    for key in hash_one:
        print(key, hash_one[key])
        hash_a.set(key, hash_one[key])
    
    for key in hash_two:
        hash_b.set(key, hash_two[key])
    # Join Hashtables
    for bucket in hash_a._buckets:
        if bucket:
            current = bucket.head
            while current:
                current_key = current.value[0]
                current_value = current.value[1]
                pairs = [current_key, current_value]

                if hash_b.contains(current_key):
                    pairs.append(hash_b.get(current_key))

                else:
                    pairs.append(None)

                answer.append(pairs)
                current = current.next

    return answer