# insertion sort algorithm
import random
import time

l = random.sample(range(1, 11), k = 10)

print(l)

def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i - 1
    next_elem = arr[i]
    while arr[j] > next_elem and j >= 0:

      arr[j + 1] = arr[j] #arr[j+1] == arr[i]
      j -= 1
      arr[j + 1] = next_elem #arr[j+1] == arr[j]
    
  return arr

ts = time.time()

print(insertion_sort(l))

te = time.time()
elapsed_time = te - ts

print(round(elapsed_time, 7))
