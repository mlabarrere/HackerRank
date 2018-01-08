#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(sum(x > 0 for x in arr)/len(arr))
print(sum(x < 0 for x in arr)/len(arr))
print(sum(x == 0 for x in arr)/len(arr))
