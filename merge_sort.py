import time
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
numtest = 10
for i in range(1, numtest + 1):
    with open("test_" + str(i) + ".txt", "r") as f:
        all_data = f.read().split()
        if all_data:
            n = int(all_data[0])
            arr = [float(x) for x in all_data[1:]]
        start_time = time.time()
        mergesort(arr)
        end_time = time.time()
        print(end_time-start_time)