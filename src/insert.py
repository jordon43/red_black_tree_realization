from RedBlackTree import RedBlackTree
import time
import math
import matplotlib.pyplot as plt

arr_time = []
arr_count = []
arr_up_logarithm = []
arr_down_logarithm = []
seconds = time.time()
COUNT = 500

for j in range(1, COUNT):
    bst_test = RedBlackTree()
    seconds = time.time()

    for i in range(j):
        bst_test.insert(j*j)

    time_1 = time.time()
    arr_time.append(float(time_1 - seconds))
    arr_count.append(j)
    time_2 = time_1

for i in range(1, COUNT):
    arr_up_logarithm.append(0.1 * math.log(i) / 200 + 0.0000015)
    arr_down_logarithm.append(0.08 * math.log(i) / 3000)

plt.figure("GRAPH")
UL = plt.subplot(111)
UL.plot(arr_count, arr_time)
UL.plot(arr_up_logarithm, color='r')
UL.plot(arr_down_logarithm, color='g')
UL.set_xlabel('Count')
UL.set_ylabel('time (s)', color='b')

plt.show()