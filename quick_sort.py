import time
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]    
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]  
    
    return quicksort(left) + middle + quicksort(right)
numtest = 10
for i in range(1, numtest + 1):
    with open("dataset/ test_" + str(i) + ".txt", "r") as f:
        all_data = f.read().split()
        if all_data:
            n = int(all_data[0])
            arr = [float(x) for x in all_data[1:]]
        start_time = time.time()
        quicksort(arr)
        end_time = time.time()

        print(end_time-start_time)
