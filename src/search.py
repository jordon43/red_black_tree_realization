from RedBlackTree import RedBlackTree
import time
import math
import matplotlib.pyplot as plt
import random

arr_count = []
arr_up_logarithm = []
arr_down_logarithm = []
arr_time_search = []
seconds = time.time()
max_key = 0
COUNT = 500

for j in range(1, COUNT):
    bst = RedBlackTree()
    arr_search = []

    for i in range(j):
        rand_num = random.randint(0, 1000000)
        bst.insert(rand_num)
        arr_search.append(rand_num)
        if rand_num > max_key:
            max_key = rand_num

    seconds_search = time.time()
    for item in arr_search:
        bst.search(max_key)
    arr_count.append(j)
    arr_time_search.append(float(time.time() - seconds_search))

for i in range(1, COUNT):
    arr_up_logarithm.append(math.log(i) / 5000 + 0.0000015)
    arr_down_logarithm.append(math.log(i) / 50000)

plt.figure("GRAPH")
UC = plt.subplot(111)
UC.plot(arr_count, arr_time_search)
UC.plot(arr_up_logarithm, color='r')
UC.plot(arr_down_logarithm, color='g')
UC.set_xlabel('Count')
UC.set_ylabel('time (s), (V)', color='b')

plt.show()