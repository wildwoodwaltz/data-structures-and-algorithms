
def insertion_sort(arr):
    for idx in range(1, len(arr)):

        val = arr[idx]

        j = idx-1

        while j >=0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
    return arr

array = [8,4,23,42,16,15]

insertion_sort(array)