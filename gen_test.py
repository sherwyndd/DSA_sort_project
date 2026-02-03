import random
#INIT
numSize = 1000000; maxVal = 1000000000; uparray = []; downarray = []; 
#GEN INCRESE TEST
for i in range(0, numSize):
    uparray.append(random.uniform(-maxVal, maxVal))
uparray.sort()
with open(str("test_1.txt"), "w", encoding = "utf-8") as f:
    f.write(str(len(uparray)) + "\n")
    for i in range(0, len(uparray)):
        f.write(str(uparray[i]) + " ")
#GEN DECREASE TEST
for i in range(0, numSize):
    downarray.append(random.uniform(-maxVal, maxVal))
downarray.sort(reverse=True)
with open(str("test_2.txt"), "w", encoding = "utf-8") as f:
    f.write(str(len(downarray)) + "\n")
    for i in range(0, len(downarray)):
        f.write(str(downarray[i]) + " ")
#GEN RANDOM INTEGER TEST
for i in range(3, 7):
    normal_array = []
    for j in range(0, numSize):
        normal_array.append(random.randint(-maxVal, maxVal))
    with open("test_" + str(i) + ".txt", "w", encoding = "utf-8") as f:
        f.write(str(len(normal_array)) + "\n")
        for j in range(0, len(normal_array)):
             f.write(str(normal_array[j]) + " ")
#GEN RANDOM FLOAT TEST
for i in range(7, 11):
    normal_array = []
    for j in range(0, numSize):
        normal_array.append(random.uniform(-maxVal, maxVal))
    with open("test_" + str(i) + ".txt", "w", encoding = "utf-8") as f:
        f.write(str(len(normal_array)) + "\n")
        for j in range(0, len(normal_array)):
             f.write(str(normal_array[j]) + " ")