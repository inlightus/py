# bubble sort algorithm

import time
import random

l = random.sample(range(1, 11), k = 10)

def bubble_sort(arr):
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(arr) - 1):
      if arr[i + 1] < arr[i]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = True
  return arr

ts = time.time()

print(bubble_sort(l))

te = time.time()
elapsed_time = te - ts

print(round(elapsed_time, 7))
