# Author: Michael Hawes
# Radix Sort

def radix_sort(mylist):
    """Sort elements by powers using buckets to store lists based on integer columns"""
    base = 10
    n = 0
    max_digit = len(str(max(mylist)))  # find max number and get length of digits

    while max_digit > n:
        bucket = [[] for _ in range(10)]        # create buckets (2D array)
        for i in mylist:      # split the lists
            bucket[i // (base ** n) % 10].append(i)        # add remainder to bucket in postion based on column
        index = 0
        for i in range(len(bucket)):       # loop through bucket
            stage_two = bucket[i]     # find lists of numbers in bucket
            for nums in stage_two:
                mylist[index] = nums     # add sorted list back into original list
                index += 1
        n += 1     # increasing the power of n


mylist = ["number list goes here"]
print(radix_sort(mylist))
