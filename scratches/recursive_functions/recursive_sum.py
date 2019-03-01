def sum_to_one(n):
    # defining the base case
    if n == 1:
        return n
    
    # adding the recursive step
    else:
        return n + sum_to_one(n-1)

print(sum_to_one(10))
print(sum_to_one(100))
