# selection sort algorithm 2

import time
import random

l = random.sample(range(1, 11), k = 10)

def selection_sort2(arr):
  for i in range(len(arr) - 1):
    i_0 = arr[i]
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
  
  return arr

ts = time.time()

print(selection_sort2(l))

te = time.time()
elapsed_time = te - ts

print(round(elapsed_time, 7))
