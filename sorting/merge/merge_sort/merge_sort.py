def merge_sort(arr):

    n = len(arr)
    print(f'Merge sorting {arr}')
    if n > 1:

        mid = n // 2

        left = arr[:mid]
        right = arr[mid:]
        
        print(f'Breaking apart into {left} and {right}')

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                arr[k] = left[i]
                print(f'since {left[i]} is smaller than {right[j]} we will add that to the next value in the list giving us {arr}')
                i += 1

            else:
                arr[k] = right[j]
                print(f'since {right[j]} is smaller than {left[i]} we will add that to the next value in the list giving us {arr}')
                j += 1
            k += 1

        if i == len(left):
            print('Since we finished with left now we need to add the rest of right')
            while j< len(right):
                arr[k] = right[j]
                k += 1
                j += 1
        else:
            print('Since we finished with left now we need to add the rest of right')
            while i < len(left):
                arr[k] = left[i]
                k += 1
                i += 1
        
        print(f'Ourproduct: {arr}')
    
    return arr

unsorted_arr = [8,4,23,42,16,15]

merge_sort(unsorted_arr)
