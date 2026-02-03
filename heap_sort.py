import time
def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
    
    return arr
numtest = 10
for i in range(1, numtest + 1):
    with open("dataset/test_" + str(i) + ".txt", "r") as f:
        all_data = f.read().split()
        if all_data:
            n = int(all_data[0])
            arr = [float(x) for x in all_data[1:]]
        start_time = time.time()
        heapsort(arr)
        end_time = time.time()

        print(end_time-start_time)
