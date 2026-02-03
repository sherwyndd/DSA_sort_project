import time
import numpy as np
numtest = 10
for i in range(1, numtest + 1):
    with open("test_" + str(i) + ".txt", "r") as f:
        all_data = f.read().split()
        if all_data:
            n = int(all_data[0])
            arr = [float(x) for x in all_data[1:]]
        start_time = time.time()
        np_arr = np.array(arr)
        sorted_arr = np.sort(np_arr)
        end_time = time.time()
        print(end_time-start_time)